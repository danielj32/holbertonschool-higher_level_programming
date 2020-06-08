#!/usr/bin/python3
""" Class Base """
import json
import csv


class Base:
    """ show class with constructor """
    __nb_objects = 0

    def __init__(self, id=None):
        """     Constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method static """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save information at the file """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jfilename:
            if list_objs is None:
                jfilename.write("[]")
            else:
                dictionary = [object.to_dictionary() for object in list_objs]
                jfilename.write(Base.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """ return repr """
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Method of class """
        if cls.__name__ == "Rectangle":
            mud = cls(3, 3)
        else:
            mud = cls(3)
        mud.update(**dictionary)
        return mud

    @classmethod
    def load_from_file(cls):
        """ Method returns a list of instances """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name) as f:
                r = f.read()
                dt = cls.from_json_string(r)
                n_list = []
                for i in dt:
                    n_list.append(cls.create(**i))
                return n_list
        except:
            pass
        return []
