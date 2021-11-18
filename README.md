# Starlamp
Note: Do not post sensitive information in this repository, it's actively shared with a public repo which will be disconnected further down the line.
T
# TODO
- [ ] galleries
  - [ ] webgl render 3d models in folder to page.
    - [ ] three.js
  - [ ] static content configuration 
    - [ ] static folder designation "static"
      - [ ] /css
      - [ ] /js
      - [ ] /assets
    - [ ] Lightbox applied to images and webgl rendered assets.
    - [ ] views.py
      - [ ] index is mandatory.
      - [ ] authored pages based on directories established in "root/media"
    - [ ] collect static assets prior to full deployment.
- [ ] accounts
  - [ ] account creation and handling (extremely basic but secure.)
- [ ] templates
  - [ ] base template for displaying global content.
  [ ] starlamp
    - [ ] urls - this will become obsolute so wtv
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




## threeJS initialization

https://threejs.org

ThreeJS is a lightweight crossbrowser general purpose 3D library that builds 
a WebGL renderer. It can also build WebGPU (experimental), SVG, and CSS3D renderers if necessary.

ThreeJS is initialized with a 'scene', much like in various other 3D applications. 
The scene is provided with a camera and the utilities to place 3D objects, which is then rendered to the browser
via WebGL. Finally, threeJS adds a viewport to the document.body element.

### threeJS API components of interest
This information here is only to give me an idea of what I'm dealing with, it's not the complete list of parameters/properties/methods by any means it's simply some that give me a better picture.

[BufferAttribute](https://threejs.org/docs/#api/en/core/BufferAttribute)
- Stores data for an attribute (vertex positions, face indices, normals, colors, UVS, and any custom attributes) associated with a BufferGeometry (a mesh, line / point geometry), which allows for more efficient passing of data to the GPU.

[Layers](https://threejs.org/docs/#api/en/core/Layers)
- Assigns object3D 1 or more of 32 layers from 0 to 31. Layers are stored as a bit mask,
**and by default all Object3Ds are member of layer 0.**
- 


[AnimationAction](https://threejs.org/docs/#api/en/animation/AnimationAction)
 - schedules a performance of animations which are stored in AnimationClips.
   - Params: **mixer**, **clip**, **localRoot**. 
   - Properties: **clampWhenFinished** (pause it on the last frame), .**loop** (can set a finite or infintie number), .**reptitions** (the number of reptitions performanced over the ocurse of the action)
   - Methods: **crossFadeFrom**, **crossFadeTo**, **play**, **setDuration**, various others.

   
[KeyframeTrack](https://threejs.org/docs/#api/en/animation/KeyframeTrack)
   - A timed sequence of keyframes composed of a list of times and related values which are used to animate a specific property of an object. 
     - Params: **name**, **times**, **values**, **interpoloation**
     - Properties: **name**, (tracks name can refer to morph targets or bones, possibly other values.)
     - Methods: .clone() (returns a copy of this track), .createInterpolant(),  .optimize() (removes equivalent sequential keys
     - Static Methods: .toJSON (self explanatory, fucking lit)

[Audio]
- Can create a non-positional global audio object for the scene, not that we'll need this.

[ArrayCamera](https://threejs.org/docs/#api/en/cameras/ArrayCamera)
- Render a scene with a predefined set of cameras.

[AmbientLight](https://threejs.org/docs/#api/en/lights/AmbientLight)
- Scene lighting and shit, illuminates all objects in the scene equally. Kinda gross but needed.
- Can set the color and intensity, but this is pretty base evel. There's various other light sources and shadow control to take advantage of.


Anyway, a ton of shit is capable with this, can't wait to really dive in.
