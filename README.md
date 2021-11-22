# Starlamp
Note: Do not post sensitive information in this repository, it's actively shared with a public repo which will be disconnected further down the line.
T
# TODO
- [ ] galleries
  - [ ] webgl render 3d models in folder to page.
    - [ ] three.js
    - [ ] NPM project files.
      - [ ] Shell file for project initalization & deployment.
        - [ ] Need to make sure all dependencies are installed properly.
  - [ ] Webpack
  - [X] static content configuration 
    - [X] static folder designation "static"
      - [X] /css
      - [X] /js
      - [X] /assets
    - [ ] Lightbox applied to images and webgl rendered assets.
    - [ ] views.py
      - [X] index is mandatory.
      - [ ] authored pages based on directories established in "root/media"
    - [ ] collect static assets prior to full deployment.
- [ ] accounts
  - [ ] account creation and handling (extremely basic but secure.)
    - [ ] Single sign on via forum account? Steam auth token? ????
- [X] templates
  - [X] base template for displaying global content.
- [ ] postgres
  - [X] migrated relations to container
- [ ] common 
  - [ ] sglib.py
    - [X] get_files()
    - [-] get_thumbs()
    - [X] get_sg_path()


# Notes
It's mandatory for a media folder to exist. There must be one subfolder within the media folder. There must be at least
ONE image or 3D asset in each gallery to serve as a thumbnail. Files are sorted alphanumerically[0-9][A-Z]. If you want a
specific picture to serve as a thumbnail, name it something like 01AA_HelloWorld.jpg or 01AA_Face.mdl

The top-level folders within the media folder are the galleries. Folders within those folders are subgalleries.
``` 
/media
-gallery-1
    -subgallery-1
    -subgallery-2
-gallery-2
    -subgallery-1
```

The models subdirectory of media refers to source engine .mdl files.

# sglib.py
get_sg_paths(filepath: string)
 - Returns a list of filepaths for all subgalleries in a given gallery.

get_files(extensions, filepath: string)
- returns a list of filepaths of one or more extensions. It can be a single extension or multiple different extensions.

get_thumbs()
- returns a list of thumbnails, the first file from every gallery discovered will be the thumbnail.



# slerror.py 

