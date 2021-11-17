from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=64)
    thumbnail = models.CharField(max_length=248)
    children = models.CharField(max_length=128)
    filepath = models.CharField(max_length=248)


class Subgallery(models.Model):
    name = models.CharField(max_length=64)
    thumbnail = models.CharField(max_length=248)
    parent = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=248)


class Images(models.Model):
    name = models.CharField(max_length=64)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    subgallery = models.ForeignKey(Subgallery, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=248)
    upload_date = models.DateField()

