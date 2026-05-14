#!/usr/bin/python3
"""
Console module for AirBnB clone.
This module creates a command interpreter for managing objects.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB Project"""

    prompt = '(hbnb) '
    # Dictionary of available classes
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do Nothing upon receiving an empty line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        import re
        import ast

        match = re.match(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if match:
            class_name = match.group(1)
            method = match.group(2)
            args_str = match.group(3)

            if class_name in self.classes:
                if method == "all":
                    return self.do_all(class_name)
                elif method == "count":
                    count = sum(1 for key in storage.all()
                                if key.startswith(class_name + "."))
                    print(count)
                    return
                elif method == "show":
                    args_str = args_str.strip('"\' ')
                    return self.do_show("{} {}".format(class_name, args_str))
                elif method == "destroy":
                    args_str = args_str.strip('"\' ')
                    return self.do_destroy(
                        "{} {}".format(class_name, args_str))
                elif method == "update":
                    dict_match = re.search(r'\{.*\}', args_str)
                    if dict_match:
                        id_str = args_str[:args_str.find(',')]
                        id_str = id_str.strip('"\' ')
                        d_str = dict_match.group(0)
                        try:
                            d = ast.literal_eval(d_str)
                            if type(d) is dict:
                                key = "{}.{}".format(class_name, id_str)
                                if key in storage.all():
                                    obj = storage.all()[key]
                                    for k, v in d.items():
                                        setattr(obj, k, v)
                                    obj.save()
                                else:
                                    print("** no instance found **")
                                return
                        except Exception:
                            pass
                    else:
                        args = args_str.split(',')
                        if len(args) >= 1:
                            id_str = args[0].strip('"\' ')
                            if len(args) == 1:
                                return self.do_update(
                                    "{} {}".format(class_name, id_str))
                            elif len(args) == 2:
                                attr_name = args[1].strip('"\' ')
                                return self.do_update(
                                    "{} {} {}".format(
                                        class_name, id_str, attr_name))
                            elif len(args) >= 3:
                                attr_name = args[1].strip('"\' ')
                                attr_val = args[2].strip('"\' ')
                                return self.do_update(
                                    "{} {} {} {}".format(
                                        class_name, id_str,
                                        attr_name, attr_val))

        print("*** Unknown syntax: {}".format(line))
        return False

    def do_create(self, arg):
        """Creates a new instance of a class, saves it and prints the id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representations of all instances"""
        args = arg.split()
        obj_list = []
        if len(args) > 0:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj))
        else:
            for key, obj in storage.all().items():
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                # Strip quotes just in case the user types the value in quotes
                val = args[3].strip('"')
                setattr(obj, args[2], val)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
