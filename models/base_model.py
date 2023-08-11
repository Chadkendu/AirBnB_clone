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

        if kwargs != {} and kwargs is not None and bool(kwargs):
            for key in kwargs:
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = dt.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """The Public instance method for the BaseModel that returns a String
        The representation of our BaseModel class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """The Public instance method that updates the `updated_at` public
         property instance"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """The Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        data = self.__dict__.copy()
        data["__class__"] = type(self).__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data
