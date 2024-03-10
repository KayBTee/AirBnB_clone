from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
    Base class for creating models with common attributes and methods.

    Attributes:
        id (str): Unique identifier for each model.
        created_at (datetime): Timestamp for creation.
        updated_at (datetime): Timestamp for update.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Sets the id to uuid4 string.
        Sets the timestamps to a UTC time.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)


        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the model

        Return:
            A string representation containing the class name, it's id, and attributes dictionary.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the new object to
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel object into dictionary representation

        Returns:
            dict: A dictionary containing the class name, id, created_at, and updated_at attributes.
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
    