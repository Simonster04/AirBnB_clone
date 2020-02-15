#!/usr/bin/python3
"""
 Containts the FileStorage Class
"""

class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    def __init__(self, file_path, objects):
        self.__file_path = file_path + ".json"
        self.__objects = {}

    def all(self):
        """ Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj = 

