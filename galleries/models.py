from django.db import models

# Create your models here.
class Subgallery(models.Model):
    name = models.CharField(max_length=128)
    parent = models.CharField(128)
    relative_path = models.CharField(248)
    absolute_path = models.CharField(248)

class Gallery(models.Model):
    name = models.CharField(max_length=128)
    thumbnail = models.CharField(max_length=248)