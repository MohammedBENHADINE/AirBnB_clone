#!/usr/bin/python3
"""
Module console, the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class HBNBCommand
    Used to handle commands and be used as interpreter/orchestror
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        'Exit the program using CTRL-D'
        print()
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'Do nothing when an empty line is entered'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
