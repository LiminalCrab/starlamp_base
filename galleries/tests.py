import os
from django.conf import settings
path = settings.MEDIA_ROOT


def get_files(extensions, fp=""):

    exts = []

    # if extensions is a list of objects, iterate over it and append it to exts.
    if len(extensions) > 1:
        for items in extensions:
            exts.append(items)

    # concat root and given filepath
    galfp = os.path.join(path, fp)

    # image names in directory to list
    prim_gallery = [img for img in os.listdir(galfp) if os.path.isfile(os.path.join(galfp, img)) if
                    img.split(".")[-1] in exts]

    if prim_gallery is None:
        raise FileNotFoundError(f"Unable to locate files.")

    # unformatted and formatted list declerations
    uffp_prim = []
    fmfp_prim = []

    # append media_root to given images
    for imgs in prim_gallery:
        uffp_prim.append(os.path.join(galfp, imgs))

    # strip the first 4 folders from the filepath
    for splits in uffp_prim:
        fmfp_prim.append("/".join(splits.strip("/").split('/')[4:]))

    print(fmfp_prim)


get_files(["mdl", "jpg"], "models")



