#!/usr/bin/python3
"""
 Containts the FileStorage Class
"""
import json
from models.base_model import BaseModel

class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dict = {}
        for key in self.__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF8') as file:
            json.dump(dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        try:
            with open(self.__file_path, 'r', encoding='UTF8') as file:
                txt = json.loads(file.read())
                for key, val in txt.items():
                    obj = BaseModel(val)
                    self.__objects[key] = obj
        except:
            pass