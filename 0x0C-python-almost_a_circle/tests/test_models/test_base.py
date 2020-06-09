#!/usr/bin/python3
""" test with unit test """
import unittest
import json
import pep8
import inspect
from models.base import Base
Base = base.Base

class Test_Base(unittest.TestCase):
    """ This test check for
        the class Base """

    @classmethod
    def setUpClass(cls):
        """ set up """
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module(self):
        """ module """
        self.assertTrue(len(base.__doc__) >= 1)
