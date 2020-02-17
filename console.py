#!/usr/bin/python3
"""
 Contains HBNBCommand class
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """

    classes_str = ['BaseModel']
    classes = [BaseModel()]

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
        aux = 0
        for cont in range(len(self.classes_str)):
            if args[0] == self.classes_str[cont]:
                obj = self.classes[cont]
                obj.save()
                print(obj.id)
                aux = 1
        if aux == 0:
            print("** class doesn't exist **")


    def do_show(self, inp):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False
        for cont in range(len(self.classes_str)):
            if args[0] == self.classes_str[cont]:
                if len(args) > 1:
                    txt = storage.all()
                    obj = args[0] + "." + args[1]
                    if obj in txt:
                        print(txt[obj])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")



    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False
        for cont in range(len(self.classes_str)):
            if args[0] == self.classes_str[cont]:
                if len(args) > 1:
                    txt = storage.all()
                    obj = args[0] + "." + args[1]
                    if obj in txt:
                        obj[txt].pop()
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


    def do_all(self, inp):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = shlex.split(inp)
        string = ""
        list = []
        for cont in range(len(self.classes_str)):
            if args[0] != self.classes_str[cont]:
                print("** class doesn't exist **")
            elif inp == "":
                for key, val in storage.all().items():
                    string = str(val)
                    list.append(string)
                print(list)
            else:
                for key, val in storage.all().items():
                    if val.__class__.__name__ == args[0]:
                        string = str(val)
                        list.append(val)
                print(list)


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