from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_images),
    path('upload/', views.upload_image),
]
