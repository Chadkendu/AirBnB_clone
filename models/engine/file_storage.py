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

    def all(self):
        ...

    def new(self):
        ...

    def save(self):
        ...

    def reload(self):
        ...
