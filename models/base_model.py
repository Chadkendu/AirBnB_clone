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
        
        if (kwargs):
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, dt.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """The Public instance method for the BaseModel that returns a String
        The representation of our BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """The Public instance method that updates the `updated_at` public
         property instance"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """The Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        data = {}
        # This iterates over all the attributes of the object
        for attr in self.__dict__:
            key = attr
            # this gets the value of the attribute
            value = getattr(self, attr)
            # this convert to string object in ISO format
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            # this collect data for serializable attributes
            data[key] = value
            # this adds the key __class__ with the name of the class object
            data['__class__'] = self.__class__.__name__
        return data
