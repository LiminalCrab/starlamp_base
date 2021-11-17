from django.db import models

class Gallery(models.Model):
    children = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    thumbnail = models.CharField(max_length=248)
    relative_path = models.CharField(max_length=248)
    absolute_path = models.CharField(max_length=248)

class Subgallery(models.Model):
    parent = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    relative_path = models.CharField(max_length=248)
    absolute_path = models.CharField(max_length=248)


class Images(models.Model):
    name = models.CharField(max_length=64)
    absolute_path = models.CharField(max_length=248)
    relative_path = models.CharField(max_length=248)
    upload_date = models.DateField()

    