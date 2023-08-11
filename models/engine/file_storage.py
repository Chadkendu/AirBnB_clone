#!/usr/bin/python3
"""This Imports some standard modules and modules from the project packages"""
import json
from models.base_model import BaseModel

"""
This is the Python class that will be responsible for the file storage.
"""


class FileStorage():
    """
    This is the class responsible for data storage for AirBnB Clone project.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self) -> dict:
        return self.__objects

    def new(self, obj: dict) -> None:
    """
    This is the public instance of the method that sets in `__objects` `obj` with
    the key
    Args:
     obj (dict) - the dictionaary object of the file
    """
    fmt = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[fmt] = obj

    def reload(self) -> None:
    """
    This is the public instance of the method that deserializes the json string into
    a dictionary object `__objects` only if the  `__file_path` exist.
    """
    try:
        with open(self.__file_path, mode="r", encoding="utf-8") as fn:
            data_strm = json.load(fn)
        for key, val in data_strm.items():
            class_name = key.split(".")[0]
            self.new(eval(class_name + "(**val)"))
    except:
        ...
