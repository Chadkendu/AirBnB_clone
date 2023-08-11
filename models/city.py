#!/usr/bin/python3
"""This would import some standard modules and modules from the project packages"""
from models.base_model import BaseModel

"""
This is the python class that models a City class but inherits from the BaseModel
class as Parent Class
"""


class City(BaseModel):
    """
    This is the class modelling the City object for the AirBnB Clone project.
    """
    name = ""
    state_id = ""
