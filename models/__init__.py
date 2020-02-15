#!/usr/bin/python3

from models.engine import file_storage
from models import base_model

storage = file_storage.FileStorage()
storage.reload()