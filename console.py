#!/usr/bin/python3
"""
 Contains HBNBCommand class
"""

import cmd
import shlex

class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, inp):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        return False

    def do_EOF(self, inp):
        """Exit the program
        """
        return True

    def do_create(self, inp):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False


    def do_show(self, inp):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False


    def do_all(self):
        """Prints all string representation of all instances
        based or not on the class name"""



    def do_update(self, inp):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file)"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False



if __name__ == '__main__':
    HBNBCommand().cmdloop()