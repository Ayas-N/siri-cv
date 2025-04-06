# BlenderProc2

[![Documentation](https://img.shields.io/badge/documentation-passing-brightgreen.svg)](https://dlr-rm.github.io/BlenderProc/)
[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DLR-RM/BlenderProc/blob/main/examples/basics/basic/basic_example.ipynb)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<p align="center">
<img src="https://user-images.githubusercontent.com/6104887/137109535-275a2aa3-f5fd-4173-9d16-a9a9b86f66e7.gif" alt="Front readme image" width=100%>
</p>

A procedural Blender pipeline for photorealistic rendering.

[Documentation](https://dlr-rm.github.io/BlenderProc) | [Tutorials](#tutorials) | [Examples](#examples) | [ArXiv paper](https://arxiv.org/abs/1911.01911) | [Workshop paper](https://sim2real.github.io/assets/papers/2020/denninger.pdf) | [JOSS article](https://joss.theoj.org/papers/10.21105/joss.04901)

## Features

* Loading: `*.obj`, `*.ply`, `*.blend`, `*.fbx`, BOP, ShapeNet, Haven, 3D-FRONT, etc.
* Objects: Set or sample object poses, apply physics and collision checking.
* Materials: Set or sample physically-based materials and textures
* Lighting: Set or sample lights, automatic lighting of 3D-FRONT scenes.
* Cameras: Set, sample or load camera poses from file.
* Rendering: RGB, stereo, depth, normal and segmentation images/sequences.
* Writing: .hdf5 containers, COCO & BOP annotations.


## Installation
### Via git

I directly cloned the Blenderproc repository, so clone this repository for access to the package.

To still make use of the blenderproc command and therefore use blenderproc anywhere on your system, make a local pip installation:

```bash
cd BlenderProc
pip install -e .
```

## Synthetic Data Generation
To run the synthetic data generation first run:

```bash
blenderproc run generate.py
```

This will runs the script that loads up the ```dune.blend``` blender scene file. It then randomises the camera location and angle whilst maintaining focus on the cube. 

Images that are generated will be placed in the ```coco_data/images``` directory. 

The bounding boxes from blenderproc are generated in the ```coco_annotations.json``` file, but this format isn't suitable for the Ultralytics package which we are using to run the YOLO model. 

To generate labels with the correct format, run:

```bash
python json_parser.py
```

Which generates bounding boxes for each corresponding image in .txt form in the ```coco_data/labels``` directory.

## YOLO Model