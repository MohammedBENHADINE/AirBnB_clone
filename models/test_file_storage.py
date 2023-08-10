#!/usr/bin/python3

from engine.file_storage import FileStorage
from base_model import BaseModel

storage = FileStorage("./file.json")
mod = BaseModel()
mod.item = 58
storage.new(mod)
#storage.save()
