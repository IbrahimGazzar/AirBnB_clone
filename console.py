#!/usr/bin/python3
"""The Console Module (command interpreter)
This module can display a prompt and take in commands.
"""

import cmd
import json
import models
from models.base_model import BaseModel
import shlex
CLASS_MAPPING = {"BaseModel": BaseModel}


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
        """
        Split the passed arguments to interpret them as console
        commands and store them in an array format
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in CLASS_MAPPING.keys():
            print("** class doesn't exist **")
            return False
        if args[0] in CLASS_MAPPING.keys():
            clas = CLASS_MAPPING.get(args[0], CLASS_MAPPING[args[0]])
            bm1 = clas()
            bm1.save()
            print(bm1.id)

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        _all = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in CLASS_MAPPING.keys():
            if len(args) > 1:
                key = args[0] + "." + args[1]
                """
                In this case if two arguments are passed, concatenate
                with dot to be able to execute the action, eg: show
                User, it will execute User.show to display user data.
                """
                if key in _all:
                    clas = CLASS_MAPPING.get(args[0], CLASS_MAPPING[args[0]])
                    bm1 = clas(**(_all[key]))
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
        _all = models.storage.all()
        if len(args) == 0:
            for key, value in _all.items():
                name = value['__class__']
                clas = CLASS_MAPPING.get(name, CLASS_MAPPING[name])
                bm = clas(**value)
                str_list.append(bm.__str__())
        elif args[0] in CLASS_MAPPING.keys():
            for key, value in _all.items():
                if value['__class__'] == args[0]:
                    clas = CLASS_MAPPING.get(args[0], CLASS_MAPPING[args[0]])
                    bm = clas(**value)
                    str_list.append(bm.__str__())
        else:
            print("** class doesn't exist **")
            return False
        print(str_list)

    def do_update(self, arg):
        """
         Updates an instance based on the class name and id by adding
        or updating attribute
        """
        cls_names = ["BaseModel"]
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls_names:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        entry_id = args[0] + "." + args[1]
        _all = models.storage.all()
        if entry_id not in _all.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False
        _all[entry_id][args[2]] = args[3]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
