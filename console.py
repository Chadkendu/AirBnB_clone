#!/usr/bin/python3
"""This would import some standard modules and needed modules from the project packages"""
import cmd
import datetime as dt
from models import storage
import re
from models.amenity import Amenities
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State

"""
This is the python class that acts as an interface for the first phase/level
of the AirBnB Clone project.
"""

all_classes = {
    "City": City,
    "User": User,
    "Place": Place,
    "Review": Review,
    "Amenities": Amenities,
    "State": State,
}


attributes = {
    "BaseModel": {
	"created_at": dt.datetime,
        "updated_at": dt.datetime
        "id": str,
    }, "User": {
	"first_name": str,
        "last_name": str
        "email": str,
        "password": str,
    }, "State": {
        "name": str
    }, "City": {
        "state_id": str,
        "name": str
    }, "Amenities": {
        "name": str
    }, "Place": {
        "city_id": str,
        "user_id": str,
        "name": str,
        "description": str,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "number_rooms": int,
        "number_bathrooms": int,
        "longitude": float,
        "amenity_ids": list
    }, "Review": {
        "place_id": str,
        "user_id": str,
        "text": str
    }
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
        if args != "":
            arg_num = args.split(" ")
            if arg_num[0] in all_classes.keys():
                for key, val in storage.all().items():
                    if type(val).__name__ == arg_num[0]:
                        list_all.append(str(val))
            else:
                print("** the class does not exist **")
                return
        else:
            for key, val in storage.all().items():
                list_all.append(str(val))
        print(list_all)

    def help_all(self) -> None:
        """This updates the help for all"""
        print("")
        print("The `all` command displays the string representation", end="")
        print(" of all the class instances present in the projet storage.\n")
        print("Usage:\n(hbnb) all the User\nor\n(hbnb) User.all()\n")

    def do_update(self, args) -> None:
        """This public instance method that will updates the specified instance of the class
        using the id and either adding more attributes or updating the
        attribute"""
        if len(args) == 0:
            print("** the class name is missing **")
            return
        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        is_match = re.search(regx, args)
        cls_name_match = is_match.group(1)
        uid_match = is_match.group(2)
        attr_match = is_match.group(3)
        val_match = is_match.group(4)
        if is_match:
            if cls_name_match in all_classes.keys():
                if uid_match:
                    id = "{}.{}".format(cls_name_match, uid_match)
                    if id in storage.all():
                        if attr_match:
                            if val_match:
                                datatype = None
                                if not re.search('^".*"$', val_match):
                                    if '.' in val_match:
                                        datatype = float
                                    else:
                                        datatype = int
                                else:
                                    val_match = val_match.replace('"', '')
                                attrs = attributes[cls_name_match]
                                if attr_match in attrs:
                                    val_match = attrs[attr_match](val_match)
                                elif datatype:
                                    try:
                                        val_match = datatype(val_match)
                                    except ValueError:
                                        pass
                                setattr(storage.all()[id], attr_match,
                                        val_match)
                                storage.all()[id].save()
                            else:
                                print("** the value is missing **")
                        else:
                            print("** the attribute name missing **")
                    else:
                        print("** sorry no instance found **")
                else:
                    print("** the instance id is missing **")
            else:
                print("** the class does not exist **")
        else:
            print("** the class name missing **")

    def help_update(self) -> None:
        """Thhis would updates the help for update"""
        print("")
        print("The `update` command updates the specified instance of a", end="")
        print(" using the class name and the ID of the instance, and", end="")
        print(" and the specifying the attribute to update or adding", end="")
        print(" a new attribute plus the value.\n")

    def do_count(self, args) -> None:
        """This is the public instance method that counts instances of class"""
        if len(args) == 0:
            print("** the class name is missing **")
            return
        arg_num = args.split(" ")
        instance_count = 0
        if arg_num[0]:
            if arg_num[0] in all_classes.keys():
                for num in storage.all():
                    if num.startswith(arg_num[0] + "."):
                        instance_count += 1
            else:
                print("** the class does not exist **")
                return
        else:
            print("** the class name is missing **")
            return
        print(instance_count)

    def help_count(self) -> None:
        """This would update the help for count"""
        print("")
        print("The `count` command wouldl displays the number of instances", end="")
        print(" of the specified class found in json file.", end="\n")
        print("Usage:\n(hbnb) the count User'\nor\n(hbnb) User.count()\n")

    def default(self, args):
        """This public instance method is called when there is an invalid command
        given. If not overwritten, it displays an error, but will
        be handling invalid commands before returning False if command doesn't
        exist."""
        arg_num = args.split(".")
        cls_name = arg_num[0]
        if cls_name in all_classes.keys() and len(arg_num) > 1:
            cmd = arg_num[1]
            cmd = cmd.replace("()", "")
            if cmd in ['all', 'count']:
                if cmd == 'all':
                    self.do_all(cls_name)
                elif cmd == 'count':
                    self.do_count(cls_name)
            else:
                if "show" in cmd:
                    id = cmd.split("(")[1].strip(")")
                    joiner = cls_name + " " + id
                    joiner = joiner.replace('"', "")
                    self.do_show(joiner)
                elif "destroy" in cmd:
                    id = cmd.split("(")[1].strip(")")
                    joiner = cls_name + " " + id
                    joiner = joiner.replace('"', "")
                    self.do_destroy(joiner)
                elif "update" in cmd:
                    clsname = cls_name
                    if "{" not in cmd.split("(")[1]:
                        cid = cmd.split("(")[1].split(", ")[0].strip(')"')
                        cr_at = cmd.split("(")[1].split(", ")[1].strip(')"')
                        up_at = cmd.split("(")[1].split(", ")[2].strip(')"')
                        joiner = "{} {} {} {}".format(clsname, cid, cr_at,
                                                      up_at)
                        print(joiner)
                        self.do_update(joiner)
                    elif len(cmd.split("(")[1].split(", {")) == 2:
                        cid = cmd.split("(")[1].split(", {")[0].strip(')"')
                        stn = cmd.split("(")[1].split(", {")[1].strip(")")
                        dic = eval("{" + stn)
                        for key, val in dic.items():
                            joiner = "{} {} {} {}".format(clsname, cid,
                                                          key, str(val))
                            print(joiner)
                            self.do_update(joiner)



if __name__ == "__main__":
    commnd = HBNBCommand()
    commnd.cmdloop()
