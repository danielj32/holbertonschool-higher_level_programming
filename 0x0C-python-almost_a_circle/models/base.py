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
