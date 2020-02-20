#!/usr/bin/python3
"""
 Contains HBNBCommand class
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interpreter """

    classes_str = ['BaseModel', 'User', 'State', 'City',
                   'Amenity', 'Place', 'Review']
    classes = [BaseModel(), User(), State(), City(), Amenity(),
               Place(), Review()]

    prompt = "(hbnb) "

    def default(self, inp):
        """ Method called to complete an input line when no command-specific
        complete_*() method is available """
        args = inp.split('.')
        for cont in range(len(self.classes_str)):
            for key in self.classes_str:
                if key == args[0]:
                    if args[1] == 'all()':
                        self.do_all(args[0])
                        return False
                    elif args[1] == 'count()':
                        cont = 0
                        for key, val in storage.all().items():
                            classe = key.split('.')
                            if args[0] == classe[0]:
                                cont += 1
                                print(cont)
                                return False
                    elif args[1][0:5] == 'show(':
                        id = args[1][5:-1]
                        line = args[0] + ' ' + id
                        self.do_show(line)
                        return False

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
                return False
        if aux == 0:
            print("** class doesn't exist **")
            return False

    def do_show(self, inp):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if not args[0] in self.classes_str:
            print("** class doesn't exist **")
            return False
        for cont in range(len(self.classes_str)):
            if args[0] == self.classes_str[cont]:
                if len(args) > 1:
                    txt = storage.all()
                    obj = args[0] + "." + args[1]
                    if obj in txt:
                        print(txt[obj])
                        return False
                    else:
                        print("** no instance found **")
                        return False
                else:
                    print("** instance id missing **")
                    return False

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if not args[0] in self.classes_str:
            print("** class doesn't exist **")
            return False
        for cont in range(len(self.classes_str)):
            if args[0] == self.classes_str[cont]:
                if len(args) > 1:
                    txt = storage.all()
                    obj = args[0] + "." + args[1]
                    if obj in txt:
                        storage.all().pop(obj)
                        storage.save()
                        return False
                    else:
                        print("** no instance found **")
                        return False
                else:
                    print("** instance id missing **")
                    return False

    def do_all(self, inp):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = shlex.split(inp)
        n_list = []
        if len(args) == 0:
            for key, val in storage.all().items():
                n_list.append(val.__str__())
            print(n_list)
            return False
        if not args[0] in self.classes_str:
            print("** class doesn't exist **")
            return False
        for cont in range(len(self.classes_str)):
            for key, val in storage.all().items():
                if val.__class__.__name__ == args[0]:
                    n_list.append(val.__str__())
            print(n_list)
            return False

    def do_update(self, inp):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file)"""
        args = shlex.split(inp)
        if len(args) == 0:
            print("** class name missing **")
            return False
        for cont in range(len(self.classes_str)):
            if not args[0] in self.classes_str:
                print("** class doesn't exist **")
                return False
            elif len(args) < 2:
                print("** instance id missing **")
                return False
            elif args[0] + '.' + args[1] not in \
                    storage.all().keys():
                print("** no instance found **")
                return False
            elif len(args) < 3:
                print("** attribute name missing **")
                return False
            elif len(args) < 4:
                print("** value missing **")
                return False
            else:
                obj = storage.all().get(args[0] + '.' + args[1])
                setattr(obj, args[2], "{}".format(args[3]))
                obj.save()
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
