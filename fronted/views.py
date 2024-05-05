from django.shortcuts import render


def list_images(request):
    return render(request, 'list_images.html')


def upload_image(request):
    return render(request, 'upload_image.html')
