#!/usr/bin/python3
"""This class Performs Test on Amenities Object"""

import unittest
from models.amenity import Amenities
from models.city import City
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.state import State


class Testamenity(unittest.TestCase):

    def test_class(self):
        new_amnty = Amenities()
        self.assertEqual(new_amnty.__class__.__name__, "Amenity")

    def test_father(self):
        new_amnty = Amenities()
        self.assertTrue(issubclass(new_amnty.__class__, BaseModel))

    def test_amenity(self):
        """This test the attributes of Class Amenities"""
        new_amnty = Amenities()
        new_amnty.name = "Free Love Care"
        self.assertEqual(new_amnty.name, 'Free Love Care')
