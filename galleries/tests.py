import os
from django.conf import settings
import itertools

path = settings.MEDIA_ROOT


def get_thumbs():
    """ Returns the first filepath inside every gallery to be used as a thumbnail."""

    # A gallery is the top most folders inside the "media/" directory.
    # Their subdirectories are considered "subgalleries"
    gallery_folder_scan = os.scandir(path)
    gallery_folder_names = []
    gallery_folder_paths = []

    unformatted_exclusion_list = []

    unformatted_image_files = []

    for gdirs in gallery_folder_scan:
        if gdirs.is_dir():
            gallery_folder_names.append(gdirs.name)

    print(f"[{len(gallery_folder_names)}] galleries discovered: {gallery_folder_names}")

    # join the media_root path to the gallery name.
    for items in gallery_folder_names:
        gallery_folder_paths.append(os.path.join(path, items))

    # Exclude these directories.
    for items in gallery_folder_paths:
        for root, subdirectories, files, in os.walk(items, topdown=True, followlinks=False):
            subdirectories[:] = [d for d in subdirectories if d not in items]
            unformatted_exclusion_list.append(subdirectories)

    exclusion_list = list(itertools.chain.from_iterable(unformatted_exclusion_list))

    print(f"[{len(exclusion_list)}] subgalleries excluded from thumbnail search: {exclusion_list}")

    # Retrieve the thumbnails from non-excluded galleries.

    for root, subdirectories, files, in os.walk(path, topdown=True, followlinks=False):
        for items in exclusion_list:
            if items in subdirectories:
                subdirectories.remove(items)
        for file in sorted(files):
            unformatted_image_files.append(os.path.join(root, file))
            break

    

get_thumbs()
