#!/usr/bin/python3
"""The Consule Module
This module can display a prompt and take in commands.
"""

import cmd
import models
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
        """
        Split the passed arguments to interpret them as console
        commands and store them in an array format
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        else:
            print("** class doesn't exist **")
            return False

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
                    print(models.storage.all()[key])
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
