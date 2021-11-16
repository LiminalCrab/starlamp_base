import os
from django.conf import settings
path = settings.MEDIA_ROOT


def get_models(fp=""):
    """ Returns a list of model filepaths within a given directory"""