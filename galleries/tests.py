import os
from django.conf import settings
from django.shortcuts import render
import itertools
path = settings.MEDIA_ROOT

# Create your tests here.
def get_sg_path(fp=""):
    """ Returns the filepaths and names of all subgalleries"""

    galfp = path + fp

    # unformatted subgallery path
    base_sg = [sdir for sdir in os.listdir(galfp) if os.path.isdir(os.path.join(galfp, sdir))]

    if len(base_sg) < 0:
        print(f"Please ensure the folder pointed to by MEDIA_ROOT is established")
    else:
        print(f"${base_sg}")


get_sg_path("/media")
