""" This defines the test cases for the BaseModel class  """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import uuid


class TestBaseModelClass(unittest.TestCase):
    """ This is the test cases for BaseModel class """

    @classmethod
    def setUpClass(cls):
        cls.first_model = BaseModel()
        cls.second_model = BaseModel()

    def test_unique_id(self):
        """ This is the test for unique id of each class instance """
        self.assertNotEqual(self.first_model.id, self.second_model.id)

    def test_instance_of_datetime(self):
        """
            This is the test that the created_at and updated_at attributes
            are instances of datetime
        """
        # This is for created_at attribute
        self.assertIsInstance(self.first_model.created_at, datetime)
        self.assertIsInstance(self.second_model.created_at, datetime)
        # This is for updated_at attribute
        self.assertIsInstance(self.first_model.updated_at, datetime)
        self.assertIsInstance(self.second_model.updated_at, datetime)

    def test_str_method(self):
        """
           This is the test that the str method returns a string in the
           format '[<class name>] (<self.id>) <self.dict>'
        """
        expected_output = (
            f"[{type(self.first_model).__name__}] "
            f"({self.first_model.id}) "
            f"{self.first_model.__dict__}"
        )
        self.assertEqual(str(self.first_model), expected_output)
