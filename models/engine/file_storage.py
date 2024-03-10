#!/usr/bin/python3


import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_name = f"{obj.__class__.name}.{obj.id}"
        setattr(self.__objects, obj_name, obj)

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        with open(self.__file_path, 'r') as f:
            self.__objects = json.load(f)
