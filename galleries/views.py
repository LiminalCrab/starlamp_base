from django.shortcuts import render
from .models import Gallery
from .models import Subgallery
from .models import Images


# The index only displays the galleries themselves. Subgalleries are displayed within galleries.


def index(req):
    return render(req, "galleries/index.html", {
        "galleries": Gallery.objects.all()
    })

