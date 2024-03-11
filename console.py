#!/usr/bin/python3
"""
Difinition of
AirBnB console
model
"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):
    """
    Definition for
    AirBnB console
    class
    """
    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    valid_int_attributes = ["number_rooms", "number_bathrooms",
                            "max_guest", "last_name"]

    valid_float_attributes = ["latitude", "longitude"]

    valid_string_attributes = ["name", "amenity_id", "place_id",
                               "state_id", "user_id", "city_id",
                               "description", "text", "email",
                               "password", "first_name", "last_name"]

    def do_create(self, arg):
        """
        Creates a new instance
        """
        av_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid_arg(arg):
            my_args = arg.split()
            if my_args[0] in av_classes:
                instance = av_classes[my_args[0]]()
                storage.save()
                print(instance.id)

    def valid_arg(self, arg, my_id=False, my_attr=False):
        """
        Validates arguments passed
        """
        my_args = arg.split()
        args_len = len(arg.split())
        if args_len == 0:
            print("** class name missing **")
            return (False)
        elif my_args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return (False)
        elif args_len < 2 and my_id:
            print("** instance id missing **")
            return (False)
        elif my_id and my_args[0]+"."+my_args[1] not in storage.all():
            print("** no instance found **")
            return (False)
        elif args_len == 2 and my_attr:
            print("** attribute name missing **")
            return (False)
        elif args_len == 3 and my_attr:
            print("** value missing **")
            return (False)
        return (True)

    def emptyline(self):
        """
        Does nothing
        when empty line
        recieved
        """
        pass

    def do_EOF(self, arg):
        """
        Ctrl-D to exit the program
        """
        return (True)

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return (True)

    def do_destroy(self, arg):
        """
        Deletes any instance
        """
        if self.valid_arg(arg, True):
            my_args = arg.split()
            my_key = my_args[0]+"."+my_args[1]
            del storage.all()[my_key]
            storage.save()

    def do_clear(self, arg):
        """
        Clears the data
        stored
        """
        storage.all().clear()
        self.do_all(arg)
        print("** All data been clear! **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        if self.valid_arg(arg, True):
            my_args = arg.split()
            my_key = my_args[0]+"."+my_args[1]
            print(storage.all()[my_key])

    def do_update(self, arg):
        """
        Updates an instance by adding or updating attribute
        """
        if self.valid_arg(arg, True, True):
            my_args = arg.split()
            my_key = my_args[0]+"."+my_args[1]
            if my_args[3].startswith('"'):
                match = re.search(r'"([^"]+)"', arg).group(1)
            elif my_args[3].stratswith("'"):
                match = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                match = my_args[3]
            if my_args[2] in HBNBCommand.valid_string_attributes:
                setattr(storage.all()[my_key], my_args[2], str(match))
            elif my_args[2] in HBNBCommand.valid_int_attributes:
                setattr(storage.all()[my_key], my_args[2], int(match))
            elif my_args[2] in HBNBCommand.valid_float_attributes:
                setattr(storage.all()[my_key], my_args[2], float(match))
            else:
                setattr(storage.all()[my_key], my_args[2],
                        self.casting(match))
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        """
        my_args = arg.split()
        _len = len(my_args)
        my_list = []
        if _len >= 1:
            if my_args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if my_args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
            print(my_list)

    def casting(self, arg):
        """ cast string to float or int if possible"""
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def _exec(self, arg):
        """Helper function parsing filtering replacing"""
        methods = {
                "all": self.do_all,
                "count": self.count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "create": self.do_create
        }
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        my_args = match[0][0]+" "+match[0][2]
        _list = my_args.split(", ")
        _list[0] = _list[0].replace('"', "").replace("'", "")
        if len(_list) > 1:
            _list[1] = _list[1].replace('"', "").replace("'", "")
        my_args = " ".join(_list)
        if match[0][1] in methods:
            methods[match[0][1]](my_args)

    def count(self, arg):
        """The number of instances of a class
        Usage: <class name>.count()\n"""
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count += 1
                print(count)

    def default(self, arg):
        """Default if there no command found"""
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(match) != 0 and match[0][1] == "update" and "{" in arg:
            _dict = re.search(r'{([^}]+)}', arg).group()
            _dict = json.loads(_dict.replace("'" '"'))
            for k, v in _dict.items():
                _arg = arg.split("{")[0]+k+", "+str(v)+")"
                self._exec(_arg)
        elif len(match) != 0:
            self._exec(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
