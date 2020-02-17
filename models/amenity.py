#!/usr/bin/python3
"""
 Contains Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialize Amenity """
        super().__init__(*args, **kwargs)
