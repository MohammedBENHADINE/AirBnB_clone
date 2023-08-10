import json
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
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        newobj = {'{}.{}'.format(obj.__class__.__name__, obj.id): print(obj)}
        self.__objects.update(newobj)

    def save(self):
        """serializes __objects to the JSON file"""
        print(self.__file_path)
        with open(self.__file_path, 'w') as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if self.__file_path != "":
            with open(self.__file_path) as fp:
                self.__objects = json.load(fp)

