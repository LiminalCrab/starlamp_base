from django.db import models


class Subgallery(models.Model):
    parent = models.CharField(128)
    name = models.CharField(max_length=128)
    relative_path = models.CharField(248)
    absolute_path = models.CharField(248)

class Gallery(models.Model):
    children = models.ForeignKey(Subgallery, on_delete=models.CASCADE, related_name="parent")
    name = models.CharField(max_length=128)
    thumbnail = models.CharField(max_length=248)