#!/usr/bin/python3
"""
This module contains the FileStorage class, which
is responsible for serializing and deserializing
the objects we will use for the AirBnB project
"""
import json


class FileStorage:
    """
    This class is responsible for handling the
    serialization and deserialization of objects
    in the AirBnB_clone project. It does this by
    taking the dictionary representation of the object
    and dumping its json representation into a file, and
    it can retrieve that representation to load a new instance
    of that object.

    Attributes:
       __file_path (str): path to the JSON file
       __objects (dict): stores all objects by <class name>.id
    """
    def __init__(self):
        """
        Intializes an instance of this class
        """
        __file_path = file.json
        __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return __objects

    def new(self, obj):
        """
        Sets a new object in __objects

        Args:
            obj (obj): object to be set with key
                <obj class name>.id
        """
        __objects[f"{type(obj)}.{obj.id}"] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        pass

    def reload(self):
        """
        Deserializes the JSON file to __objects. If __file_path
        is empty or doesn't exist, it does nothing
        """
        pass
