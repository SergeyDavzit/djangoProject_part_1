from rest_framework import serializers
from .models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return ImageModel.objects.create(**validated_data)

    class Meta:
        model = ImageModel
        fields = '__all__'
