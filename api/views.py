from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ImageModel
from .serializers import ImageSerializer


@api_view(['POST', 'GET', 'DELETE'])
def image(request):
    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        queryset = ImageModel.objects.all()
        if len(queryset) == 0:
            return Response([])
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        print(request.data)
        obj = ImageModel.objects.filter(image_id=request.data['image_id'])
        if obj.exists():
            image_id = obj[0].image_id
            obj.delete()
            return Response({'image_id': image_id}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)