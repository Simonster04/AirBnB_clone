#!/usr/bin/python3
"""
 Containts the FileStorage Class
"""

import json
import gc
from models.base_model import BaseModel
import os.path as path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place, 'Review': Review}


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
            file.write(json.dumps(dict))

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path))"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF8') as file:
                txt = file.read()
            if len(txt) > 0:
                dic = json.loads(txt)
                for key, val in dic.items():
                    obj = classes[val["__class__"]](**val)
                    self.__objects[key] = obj
