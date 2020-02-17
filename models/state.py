#!/usr/bin/python3
"""
 Contains State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialize State """
        super().__init__(*args, **kwargs)
