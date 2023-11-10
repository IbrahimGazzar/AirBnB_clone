#!/usr/bin/python3
"""The Consule Module
This module can display a prompt and take in commands.
"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
