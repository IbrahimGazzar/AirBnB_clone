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
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects

        Args:
            obj (obj): object to be set with key
                <obj class name>.id
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """
        Deserializes the JSON file to __objects. If __file_path
        is empty or doesn't exist, it does nothing
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                self.__objects = json.load(fp)
        except FileNotFoundError:
            pass
