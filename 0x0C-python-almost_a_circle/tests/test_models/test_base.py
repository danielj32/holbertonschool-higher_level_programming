#!/usr/bin/python3
""" test with unit test """
import unittest
import json
import pep8
import inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ This test check for
        the class Base """

    @classmethod
    def setUpClass(cls):
        """ set up """
        pass

    @classmethod
    def tearDown(cls):
        """ only argument """
        pass
