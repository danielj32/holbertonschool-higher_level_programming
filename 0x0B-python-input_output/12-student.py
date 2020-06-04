#!/usr/bin/python3
""" Class Student """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Construct """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Class to dictionary """
        return self.__dict__

    def to_json(self, attrs=None):
        """ returns directory description with filter """

        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        r = {}
        for ct in attrs:
            if not isinstance(ct, str):
                return self.__dict__
            if ct in self.__dict__.keys():
                r[ct] = self.__dict__[ct]
        return r
