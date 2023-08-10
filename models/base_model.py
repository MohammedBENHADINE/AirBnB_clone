#!/usr/bin/python3
import uuid
from datetime import datetime
"""
Module that defines a Class BaseModel
"""


class BaseModel:
    """Class BaseModel defines all common attributes/methods for other classes

    Attributes:
        id (string): identifier of the instance
            created with uuid module
        created_at (datetime): date of creation of the instance
            assign with the current datetime when an instance is created
        updated_at (datetime): last date of update
             assign with the current datetime when an instance is created\
                     and it will be updated every time you change your object
    Methods:
        save (self): updates the public instance attribute updated_at with\
                the current datetime
        to_dict (self): returns a dictionary containing all keys/values of\
                __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """instantiation time"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key != '__class__'):
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)

    def save(self):
        """Update the instance"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Serialiization process
        create a dict representation with "simple object type" of BaseModel
        """
        newdict = dict(self.__dict__)
        newdict['created_at'] = datetime.isoformat(self.created_at)
        newdict['updated_at'] = datetime.isoformat(self.updated_at)
        newdata = {'__class__': self.__class__.__name__}
        newdict.update(newdata)
        return newdict

    def __str__(self):
        """Should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
