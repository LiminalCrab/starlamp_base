import os
from django.conf import settings

path = settings.MEDIA_ROOT


def get_images(fp=""):
    """ Returns all images within a given directory, does not crawl subdirectories."""

    exts = ["jpg", "jpeg", "png", "gif"]

    try:

        # concat root and given filepath
        galfp = os.path.join(path, fp)

        # image names in directory to list
        prim_gallery = [img for img in os.listdir(galfp) if os.path.isfile(os.path.join(galfp, img)) if img.split(".")[-1] in exts]

        if prim_gallery is None:
            raise FileNotFoundError(f"Unable to locate files.")

        # unformatted and formatted list declerations
        uffp_prim = []
        fmfp_prim = []

        # append media_root to given images
        for imgs in prim_gallery:
            uffp_prim.append(os.path.join(galfp, imgs))

        for splits in uffp_prim:
            fmfp_prim.append(splits[:1])
            print(fmfp_prim)

    finally:
        print(fmfp_prim)

get_images("models")