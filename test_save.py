#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

print("Testing save")
fs = FileStorage()
bm = BaseModel()
bm.save()
print("BaseModel save done")

print("Testing __objects")
print(type(fs._FileStorage__objects) == dict)

print("Testing reload")
fs.reload()
print("Reload done")
