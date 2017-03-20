#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class Hosh(cmd.Cmd):
    """
    Hosh is a command console which allows for manipulation and storage of
    different class objects
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Review", "Place"]
    file = None

    def preloop(self):
        """Create custom class functions upon console initialization"""
        self.create_class_methods()

    def do_count(self, arg):
        """Count all of the objects currently stored"""
        count = 0
        if len(arg) == 0:
            for key in storage.all().keys():
                count += 1
            print(count)
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        for key in storage.all().keys():
            if storage.all()[key].__class__.__name__ == arg:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update or create a new attribute for an object"""
        obj = find_object(self, arg)
        if obj is None:
            return
        args = arg.split(' ')
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()

    def do_all(self, arg):
        """Print all objects stored"""
        if len(arg) == 0:
            for key in storage.all().keys():
                print(storage.all()[key])
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        for key in storage.all().keys():
            if storage.all()[key].__class__.__name__ == arg:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an object"""
        obj = find_object(self, arg)
        if obj is not None:
            del storage.all()[obj.id]
            storage.save()

    def do_show(self, arg):
        """Print out an object"""
        obj = find_object(self, arg)
        if obj is not None:
            print(obj)

    def do_create(self, arg):
        """Create a new BaseModel object"""
        args = arg.split(' ')
        new_model = eval(args[0] + "()")
        new_model = find_attributes(new_model, args)
        new_model.save()
        print("{}".format(new_model.id))

    def do_quit(self, arg):
        """Quit the current hbnb shell session"""
        return True

    def do_EOF(self, arg):
        """Quit the current hbnb shell session"""
        print()
        return True

    def emptyline(self):
        """Do nothing when entered an empty line"""
        pass

    def create_class_methods(self):
        """Create a do_<cls> method for each existing class"""
        for cls in self.classes:
            self.create_method(cls)

    def create_method(self, cls):
        """Create a do_<cls> method for a class"""
        def class_method(self, arg):
            """Parses arg line and formats a string to use existing methods"""
            args = arg.split('(')
            if args[0][:1] == '.' and args[1][-1:] == ')':
                formatted_arg = class_method.__name__[3:] + " " + args[1][:-1]
                l = formatted_arg.split(' ')
                value = ''
                if len(l) > 4:
                    print("too many arguments")
                    return
                if len(l) > 3:
                    value = l[3].replace("'", '"')
                if len(l) > 1:
                    formatted_arg = ""
                    for item in l[:-1]:
                        formatted_arg += " " + item.strip(',')
                formatted_arg = formatted_arg + " " + value
                formatted_arg = formatted_arg.strip(' ')
                print(formatted_arg)
                exec("self.do_{:s}('{:s}')".format(args[0][1:], formatted_arg))
        docstring = "Execute method for {} based on argument".format(cls)
        class_method.__doc__ = docstring
        class_method.__name__ = "do_{}".format(cls)
        setattr(self.__class__, class_method.__name__, class_method)


def find_attributes(new_obj, args):
    """
    Add extra attributes of the format:
        $ create <classname> <param1="value"> <param2=number>
    An indefinite number of arguments is allowed.
    """
    if len(args) > 1:
        i = 0
        for arg in args:
            i += 1
            if i > 1:
                if '=' in arg:
                    arg = arg.split('=')
                    name = arg[0]
                    value = arg[1][1:-1]
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            if arg[1][0] == '"' and arg[1][-1] == '"':
                                value = value.replace('_', ' ')
                                setattr(new_obj, name, value)
                            else:
                                print("attribute of name {} needs quotes \
                                around it".format(arg[1]))
    return new_obj


def find_object(self, arg):
    """Find an object based on class and id"""
    if len(arg) == 0:
        print("** class name missing **")
        return None
    args = arg.split(' ')
    if len(args) < 2:
        print("** instance id missing **")
        return None
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return None
    stored_objects = storage.all()
    for object_id in stored_objects.keys():
        if object_id == args[1]:
            return stored_objects[object_id]
    print("** no instance found **")
    return None

if __name__ == "__main__":
    Hosh().cmdloop()
