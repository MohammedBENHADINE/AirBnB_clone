import json
import os.path
"""
Module that implements the Class FileStorage
"""


class FileStorage:
    """Class FileStorage
    serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (string): Path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id

    Methods:
        all (self): returns the dictionary __objects
        new (self, obj): sets in __objects the obj with key <obj class name>.id
        save (self): serializes __objects to the JSON file
        reload (self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        newkey = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[newkey] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_objs = {
                key: obj.to_dict() for key, obj in self.__objects.items()
                }
        with open(self.__file_path, 'w') as fp:
            json.dump(serialized_objs, fp)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as fp:
                serialized_objs = json.load(fp)
                from models.base_model import BaseModel
                for key, obj in serialized_objs.items():
                    if obj is not None:
                        self.__objects[key] = BaseModel(**obj)
