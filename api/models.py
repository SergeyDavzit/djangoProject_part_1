from django.db import models


class ImageModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_data = models.TextField()
    description = models.TextField()
