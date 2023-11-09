#!/usr/bin/python3
"""
This module contains the BaseModel class for the AirBnB clone project,
from which all other models will inherit their base and common features and
attributes from.
"""
import datetime
import uuid


class BaseModel():
    """
    The base model from which all other classes in the AirBnB project will
    inherit their basic and common features and attributes from.

    Attributes:
        id (str): unique id created by uuid for every instance of.
        created_at (datetime): datetime when an instance is created.
        updated_at (datetime): datetime when an instance is created
            and it will be updated every time you change your object.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization function that sets up all the main attributes
        """
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Function that returns the string representation of basemodel,
        following this format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        dicti = dict(self.__dict__)
        dicti['__class__'] = type(self).__name__
        dicti['created_at'] = dicti['created_at'].isoformat()
        dicti['updated_at'] = dicti['updated_at'].isoformat()
        return dicti
