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
    """ This test check for the class Base """

    @classmethod
    def setUpClass(cls):
        """ set up """
        pass

    @classmethod
    def tearDown(cls):
        """ only argument """
        pass

    def test_pep8(self):
        """ Test that models/base.py conforms to PEP8 """
        pepstyle = pep8.StyleGuide(quiet=True)
        result = pepstyle.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")
