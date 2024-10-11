# czi-scenes

A simple utility to get scene information from a Zeiss czi file

## Installation
pip install git+https://github.com/pnewstein/czi-scenes

## Command line usage
```bash
czi-scenes example.czi
```

## Python API
```python
import czi_scenes
from pylibCZIrw import czi

path = "example.czi"
with czi.open_czi(path) as czi_file:
    metadata = czi_file.raw_metadata
scene_info = czi_scenes.read_scene_information_from_xml_str(metadata)
```
