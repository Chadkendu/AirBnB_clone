#!/usr/bin/python3
"""This Imports some standard modules and modules from the project packages"""
import json
from datetime import datetime as dt
from models.place import Place
from models.amenities import Amenities
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.review import Review

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
        return FileStorage.__objects

    def new(self, obj: dict) -> None:
    """
    This is the public instance of the method that sets in `__objects` `obj` with
    the key
    Args:
     obj (dict) - the dictionaary object of the file
    """

    obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
    FileStorage.__objects[obj_key] = obj

    def save(self) -> None:
    """
    This is a public instance method that serializes the private instance
    object `__objects` (dict) into a JSON string and save it to a flat
    database (json file)
    """
    dict_serial = {}
    with open(self.__file_path, mode="w", encoding="utf-8") as file_obj:
        for key, val in self.__objects.items():
            dict_serial[key] = val.to_dict()
            json.dump(dict_serial, file_obj)

    def reload(self) -> None:
    """
    This is the public instance of the method that deserializes the json string into
    a dictionary object `__objects` only if the  `__file_path` exist.
    """
    try:
        path = self.__file_path
        with open(path, mode="r", encoding="utf-8") as file_obj:
            data_strm = json.load(file_obj)
        for key, val in data_strm.items():
            class_name = key.split(".")[0]
            self.new(eval(class_name + "(**val)"))
    except FileNotFoundError:
        pass
