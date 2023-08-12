#!/usr/bin/python3
"""This class Performs Test on State Object"""

import unittest
from models.amenity import Amenities
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State


class Teststate(unittest.TestCase):

    def test_class(self):
        new_state = State()
        self.assertEqual(new_state.__class__.__name__, "State")

    def test_container(self):
        new_state = State()
        self.assertEqual(new_state.__class__.__name__, "State")

    def test_state(self):
        """
        This test attributes of State Object
        """
        new_state = State()
        new_state.name = "Memphis"
        self.assertEqual(new_state.name, 'Memphis')
