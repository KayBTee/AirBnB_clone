
from uuid import uuid4
from datetime import datetime


class BaseModel:
    
    def __init__(self, id):
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[self.__name__] (self.id) self.__dict__"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__
