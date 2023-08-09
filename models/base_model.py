#!/usr/bin/python3
""" Function that defines the BaseModel class """
import uuid
from datetime import datetime


class BaseModel:
    """ This defines all common attributes or methods for other classes """

    def __init__(self):
        """ Initialize instances """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ This returns the string representation of the instance """
        str_rep = "[{}] ({}) {}"
        cls_name = __class__.__name__
        return (str_rep.format(cls_name, self.id, self.__dict__))

    def save(self):
        """ This Updates updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ This returns a dictionary containing all keys or values
            of __dict__ of an instance
        """
        data = {}
        # This iterate over all the attributes of the object
        for attr in self.__dict__:
            key = attr
            # This get the value of the attribute
            value = getattr(self, attr)
            # This convert to string object in ISO format
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            # This collect data for serializable attributes
            data[key] = value
            # This add the key __class__ with name of the class object
            data['__class__'] = self.__class__.__name__
        return data
