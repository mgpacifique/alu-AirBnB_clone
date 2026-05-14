#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serialize insances to a JSON file and
    deserialization back to instances
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj classname>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists"""
        classes = {"BaseModel": BaseModel}
        try:
            from models.user import User
            classes["User"] = User
        except ImportError:
            pass
        try:
            from models.state import State
            classes["State"] = State
        except ImportError:
            pass
        try:
            from models.city import City
            classes["City"] = City
        except ImportError:
            pass
        try:
            from models.amenity import Amenity
            classes["Amenity"] = Amenity
        except ImportError:
            pass
        try:
            from models.place import Place
            classes["Place"] = Place
        except ImportError:
            pass
        try:
            from models.review import Review
            classes["Review"] = Review
        except ImportError:
            pass

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name = value['__class__']
                        if class_name in classes:
                            obj = classes[class_name](**value)
                            FileStorage.__objects[key] = obj
                except Exception:
                    pass
