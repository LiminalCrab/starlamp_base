from django.shortcuts import render
from .models import Gallery
from .models import Subgallery
from .models import Images

# Create your views here.


def index(req):
    return render(req, "galleries/index.html", {
        "galleries": Gallery.objects.all()
    })

