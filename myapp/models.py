from django.db import models
from django.db.models.base import Model

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to="myimages")
    date = models.DateTimeField(auto_now_add=True)

