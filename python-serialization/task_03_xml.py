#!/usr/bin/python3
"""
Serialize and deserialize a Python dictionary using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)
    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text if child.text is not None else ""

        return data
    except Exception:
        return None
