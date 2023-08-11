#!/usr/bin/python3
"""This would import some standard modules and needed modules from the project packages"""
import json
import cmd
from models import storage
from models.base_model import BaseModel


"""
This is the python class that acts as an interface for the first phase/level
of the AirBnB Clone project.
"""

all_classes = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    """
    This is the class modelling the inteface for AirBnB Clone project.
    """

    """This specifies the prompt for the CLI"""
    prompt = "(hbnb) "

    def do_quit(self, arg: any) -> None:
        """This issues the quit command to the CLI"""
        exit(1)

    def help_quit(self) -> None:
        """This updates the helps for quit"""
        print("")
        print("The `quit` command issues a command to quit the CLI.\n")
        print("Usage:\n(hbnb) quit\n")

    def do_EOF(self, arg: any) -> True:
        """This returns True and breaks out the cmdloop"""
        print("")
        return True

    def help_EOF(self) -> None:
        """This updates the help for EOF"""
        print("")
        print("The `EOF` command returns True to break the cmdloop", end=" ")
        print("and exits the CLI.\n")
        print("Usage:\n(hbnb) EOF\nor\n(hbnb) <CTRL + C>")
        print("or\n(hbnb) <CTRL + Z>\n")

    def emptyline(self) -> None:
        ...

    def do_create(self, args) -> None:
        """This is a public instance method that creates new instance of a class, save
        to a JSON file & print the `id` of the instance"""
        if len(args) == 0:
            print("** the class name is missing **")
            return
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            obj = eval(arg_num[0] + "()")
            id = getattr(obj, 'id')
            print(id)
            storage.save()
            return
        else:
            print("** the class doesn't exist **")
            return

    def help_create(self) -> None:
        """This updates the help for create"""
        print("")
        print("The `create` command creates the instance of the class, ", end="")
        print("saves it to the storage and prints out the ID of the", end=" ")
        print("instance that was created.\n")
        print("Usage:\n(hbnb) create new User\n")

    def do_show(self, args=None) -> None:
        """The public instance method that will display the string instance of the class,
        based on the instance id and classname that was specified"""
        if len(args) == 0:
            print("** the class name is missing **")
            return
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            if len(arg_num) >= 2:
                id = "{}.{}".format(arg_num[0], str(arg_num[1]))
                str_obj = storage.all()
                if id in str_obj.keys():
                    obj = str_obj[id]
                    print(obj)
                    return
                else:
                    print("** there is no instance found **")
                    return
            else:
                print("** the instance id missing **")
                return
        else:
            print("** the class doesn't exist **")
            return

    def help_show(self) -> None:
        """This updates the help for show"""
        print("")
        print("The `show` command displays the details and string", end=" ")
        print("representation of the instance based on the class name", end=" ")
        print("and instance id provided in the project.\n")
        print("Usage:\n(hbnb) show User id 51a155c1-214a-4923-8d53-523900fed722")
        print("")

    def do_destroy(self, args) -> None:
        """This public instance method that will delete the instance of the class,
        based on the instance id and classname that was specified"""
        if len(args) == 0:
            print("** the class name missing **")
            return
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            if len(arg_num) == 2:
                id = "{}.{}".format(arg_num[0], str(arg_num[1]))
                str_obj = storage.all()
                if id in str_obj.keys():
                    del (str_obj[id])
                    storage.save()
                    return
                else:
                    print("** there is no instance found **")
                    return
            else:
                print("** the instance id missing **")
                return
        else:
            print("** the class doesn't exist **")
            return

    def help_destroy(self) -> None:
        """This updates the help for destroy"""
        print("")
        print("The `destroy` command deletes all the details of an ", end="")
        print("instance based on the class name and instance id provided.\n")
        print("Usage:\n(hbnb) destroy User. 51a155c1-214a-4923-8d53-52fed22\n")

    def do_all(self, args) -> None:
        """The public instance method that will display the string instance of all
        instances of the class based on the classname that was specified or if no
        classname specified"""
        list_all = []
        str_obj = storage.all()
        arg_num = args.split(" ")
        if len(args) == 0:
            for obj in str_obj.values():
                list_all.append(str(obj))
        elif arg_num[0] in all_classes.keys():
            for id in str_obj.keys():
                if id.split(".")[0] == arg_num[0]:
                    list_all.append(str(str_obj[id]))
        else:
            print("** the class doesn't exist **")
            return
        print(list_all)

    def help_all(self) -> None:
        """This updates the help for all"""
        print("")
        print("The `all` command displays the string representation", end="")
        print(" of all the class instances present in the projet storage.\n")
        print("Usage:\n(hbnb) show all User\n")

    def do_update(self, args) -> None:
        """This public instance method that will updates the specified instance of the class
        using the id and either adding more attributes or updating the
        attribute"""
        if len(args) == 0:
            print("** the class name missing **")
            return
        str_obj = storage.all()
        arg_num = args.split(" ")
        if arg_num[0] in all_classes.keys():
            if len(arg_num) >= 2:
                for id in str_obj.keys():
                    if arg_num[1] in id.split(".")[1]:
                        id = "{}.{}".format(arg_num[0], arg_num[1])
                        obj = str_obj[id]
                        if len(arg_num) < 3:
                            print("** the attribute name missing **")
                            return
                        elif len(arg_num) < 4:
                            print("** the value missing **")
                            return
                        else:
                            try:
                                setattr(obj, arg_num[2],
                                        eval(arg_num[3].strip('"')))
                            except Exception:
                                setattr(obj, arg_num[2],
                                        arg_num[3].strip('"'))
                            storage.save()
            else:
                print("** there is no instance found **")
                return
        else:
            print("** the class doesn't exist **")
            return

    def help_update(self) -> None:
        """Thhis would updates the help for update"""
        print("")
        print("The `update` command updates the specified instance of a", end="")
        print(" using the class name and the ID of the instance, and", end="")
        print(" and the specifying the attribute to update or adding", end="")
        print(" a new attribute plus the value.\n")


if __name__ == "__main__":
    try:
        commnd = HBNBCommand()
        commnd.cmdloop()
    except (KeyboardInterrupt, EOFError):
        exit(1)