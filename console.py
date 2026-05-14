#!/usr/bin/python3"""
# Console module for AirBnB clone.
# This module creates a command interpreter for managing objects.
# """
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB Project"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do Nothing upon receiving an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
