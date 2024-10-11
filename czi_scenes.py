"""
Reads scene names from a czi file
"""
import xml.etree.ElementTree as ET
import sys

from czifile import CziFile

def read_scene_information_from_xml_str(xml: str) -> list[dict[str, str]]:
    """
    returns a list where each dict has two elemnts: "Index" and "Name"
    """
    tree = ET.fromstring(xml)
    scenes_path = "./Metadata/Information/Image/Dimensions/S/Scenes"
    scenes_node = tree.find(scenes_path)
    assert scenes_node is not None
    out: list[dict[str, str]] = []
    for node in scenes_node:
        out.append(node.attrib)
    return out


def main():
    """
    takes path from the argument and prints out information about the scene
    names
    """
    try:
        path = sys.argv[1]
    except IndexError:
        print("Please provide path", file=sys.stderr)
        sys.exit(1)
    with CziFile(path) as czi_file:
        metadata = czi_file.metadata(raw=True)
    assert isinstance(metadata, str)
    scene_info = read_scene_information_from_xml_str(metadata)
    for scene in scene_info:
        print(scene)
