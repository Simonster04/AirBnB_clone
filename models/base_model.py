#!/usr/bin/python3
"""
Contains the BaseModel class
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        timeform = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, datetime.strptime(val, timeform))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ prints as string """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
        __dict__ of the instance """
        aux = self.__dict__.copy()
        for key, val in aux.items():
            if key == "created_at" or key == "updated_at":
                aux[key] = val.isoformat()
            else:
                aux[key] = val
        aux['__class__'] = self.__class__.__name__
        return aux
