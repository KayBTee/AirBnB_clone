#!/usr/bin/python3


import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_name] = obj

    def save(self):
        try:
            ser_objs = {}
            for key, value in self.__objects.items():
                ser_objs[key] = value.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(ser_objs, f, default=str)
        except Exception as e:
            print(e)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except Exception as e:
            self.__objects = {}
