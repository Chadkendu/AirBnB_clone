""" This defines the test cases for the BaseModel class  """

import unittest
from models.base_model import BaseModel
import os
import uuid
from datetime import datetime


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

    def test_save_method(self):
        """
           This is the test that the save method updates the
           updated_at attribute to current datetime
        """
        initial = self.first_model.updated_at
        updated = self.first_model.save()
        self.assertNotEqual(initial, updated)

    def test_to_dict_method(self):
        """
           This is the test that the to_dict method returns a dictionary
           representation of object with all the instance attributes set
        """
        self.assertIsInstance(self.first_model.to_dict(), dict)

    def test_ISO_format(self):
        """
           This is the test that the created_at and updated_at attributes
           are converted to string objects in the ISO format specified.
           This makes use of the regular expression to match the patterns.
        """
        obj = self.first_model.to_dict()
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}"
        self.assertRegex(str(obj['created_at']), pattern)
        self.assertRegex(str(obj['updated_at']), pattern)

    def test_recreate_instance(self):
        """
           This test that the instance is re-created from its
           dictionary representaions
        """
        obj_json = self.first_model.to_dict()
        new_obj = BaseModel(**obj_json)
        # passes if objects are different
        self.assertIsNot(obj_json, new_obj)

    def test_datetime_objects(self):
        """
           This test that the created_at and updated_at attributes are
           converted correctly from the string form to datetime object
        """
        obj_json = self.first_model.to_dict()
        new_obj = BaseModel(**obj_json)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)

    def test_attributes(self):
        """
           This test that dictionary representation is returned by
           to_dict method which does not contain any private attributes
           of the instance.
           __class__ is not included
        """
        obj_json = self.first_model.to_dict()
        vars_dict = vars(self.first_model)
        for key in obj_json:
            if key == '__class__':
                continue
            self.assertIn(key, vars_dict)
