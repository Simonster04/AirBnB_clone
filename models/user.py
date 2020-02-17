#!/usr/bin/python3
"""
 Contains class User
 """

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initialize user """
        super().__init__(*args, **kwargs)
