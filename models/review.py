#!/usr/bin/python3
"""
 Contains Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initialize Review """
        super().__init__(*args, **kwargs)
