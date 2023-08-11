#!/usr/bin/python3
"""This would import some standard modules and modules from the project packages"""
from models.base_model import BaseModel

"""
This is the python class that models a State class but inherits
BaseModel class as the Parent Class
"""


class State(BaseModel):
    """
    This is the class modelling the State object for the AirBnB Clone project.
    """
    name = ""
