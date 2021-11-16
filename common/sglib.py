import os
from django.conf import settings
from django.shortcuts import render
import itertools

path = settings.MEDIA_ROOT


def get_sg_path(fp=""):
    """ Returns a relative filepath of all subgalleries within the a given folder in /media"""

    galfp = os.path.join(path, fp)

    # subgalleries within all top-level folders of /media
    base_sg = [sdir for sdir in os.listdir(galfp) if os.path.isdir(os.path.join(galfp, sdir))]

    if base_sg is None:
        raise NameError("Unable to locate files.")

    uf_sg = []
    fm_sg = []

    for sdirs in base_sg:
        uf_sg.append(os.path.join(galfp, sdirs))


    # this is bad code, fix the hardcoded value later.
    for splits in uf_sg:
        fm_sg.append(splits[36:])


    return fm_sg

