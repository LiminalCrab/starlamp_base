import os
from django.conf import settings
import itertools

path = settings.MEDIA_ROOT


def get_sg_path(fp=""):
    """ Returns a list of filepaths of all subgalleries within the a given folder in /media"""

    galfp = os.path.join(path, fp)

    # subgalleries within all top-level folders of /media
    base_sg = [sdir for sdir in os.listdir(galfp) if os.path.isdir(os.path.join(galfp, sdir))]

    if base_sg is None:
        raise NameError("Unable to locate files.")

    uf_sg = []
    fm_sg = []

    for sdirs in base_sg:
        uf_sg.append(os.path.join(galfp, sdirs))

    # strip the first 4 folders from the filepath
    for splits in uf_sg:
        fm_sg.append("/".join(splits.strip("/").split('/')[4:]))

    return fm_sg


def get_files(extensions, fp=""):
    """Returns specified filetype from a given directiory.
    Can take a single extension .jpg or a list [".jpg", ".mdl"]."""

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

    return fmfp_prim


def get_thumbs():
    """ Returns the first filepath inside every gallery to be used as a thumbnail."""

    # A gallery is the top most folders inside the "media/" directory.
    # Their subdirectories are considered "subgalleries"
    gallery_folder_scan = os.scandir(path)
    gallery_folder_names = []
    gallery_folder_paths = []

    unformatted_exclusion_list = []

    unformatted_image_filepath = []
    formatted_image_filepath = []

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
            unformatted_image_filepath.append(os.path.join(root, file))
            break

    # format the path properly.
    for paths in unformatted_image_filepath:
        formatted_image_filepath.append("/".join(paths.strip("/").split('/')[4:]))

    return formatted_image_filepath

