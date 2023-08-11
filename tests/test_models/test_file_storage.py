""" This file defines test cases for the Filestorage class """

import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorageClass(unittest.TestCase):
    """ This is the test cases for the FileStorage class """

    def test_private_class_instance(self):
        """
           This is the test that the __file_path and __objects attributes are
           initialized with correctly and when a new instance of FileStorage is created
        """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all_returns_dict(self):
        """ This is the test that the all() method returns a dictionary """
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIs(obj_dict, storage._FileStorage__objects)

    def test_new_method(self):
        """
           This is the test that the new() method adds an object
        """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage._FileStorage__objects.keys())
        self.assertIs(storage._FileStorage__objects[key], obj)
