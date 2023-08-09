#!/usr/bin/python3
"""This imports some Standard modules and modules from the project packages"""
from datetime import datetime as dt
import uuid as uid
import models

"""
This is the Python class that will use Base class or Parent class from which
the other classes will inherit.
"""


class BaseModel():
    """
    This is the class modelling BaseModel object for the AirBnB Clone project.
    """
    def __init__(self, *args, **kwargs) -> None:
        """This is the constructor for the BaseModel class that makes and instance
        an instances of the BaseModel object when created.
        Args:
            args (any) - the non-keyworded arguments
            kwargs (any) - the keyworded key and valued paired arguments
        """
        if bool(kwargs) is True and len(kwargs) > 0:
            for key_attr, attr_value in kwargs.items():
                if key_attr != "__class__":
                    setattr(self, key_attr, attr_value)
                elif key_attr in ['created_at', 'updated_at']:
                    setattr(self, key_attr,
                            dt.strptime(attr_value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at

    def __str__(self) -> str:
        """The Public instance method for the BaseModel that returns a String
        The representation of our BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """The Public instance method that updates the `updated_at` public
        instance property"""
        self.updated_at = dt.now()

    def to_dict(self) -> dict:
        """The Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        new_dict = dict(self.__dict__)
        new_dict['id'] = self.id
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return new_dict
