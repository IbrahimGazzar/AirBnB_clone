#!/usr/bin/python3
"""The Console Module (command interpreter)
This module can display a prompt and take in commands.
"""

import cmd
import json
import models
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """Command processor class."""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Function to exit the program."""
        return True

    def do_EOF(self, line):
        """Function to exit the program."""
        return True

    def emptyline(self):
        """
        Prevents execution of the previous command when
        an empty line is entered.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of a class"""
        args = shlex.split(line)
        cls_names = ["BaseModel"]
        """
        Split the passed arguments to interpret them as console
        commands and store them in an array format
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls_names:
            print("** class doesn't exist **")
            return False
        if args[0] == "BaseModel":
            bm1 = BaseModel()
            bm1.save()
            print(bm1.id)

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0]:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                """
                In this case if two arguments are passed, concatenate
                with dot to be able to execute the action, eg: show
                User, it will execute User.show to display user data.
                """
                if key in models.storage.all():
                    bm1 = BaseModel(**(models.storage.all()[key]))
                    print(bm1)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0]:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name
        """
        args = shlex.split(arg)
        str_list = []
        class_mapping = {"BaseModel": BaseModel}
        if len(args) == 0:
            for key, value in models.storage.all().items():
                name = value[__class__]
                clas = class_mapping.get(name, class_mapping[name])
                bm = clas(**value)
                str_list.append(bm.__str__())
        elif arg[0] == "BaseModel":
            for key, value in models.storage.all.items():
                if value[__class__] == "BaseModel":
                    bm = BaseModel(**value)
                    str_list.appened(bm.__str__())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
