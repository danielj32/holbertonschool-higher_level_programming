#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        """ Class of testing """

        def first_test(self):
                n_list = [100, 200, 400]
                self.assertEqual(max_integer(n_list), 400)

        def second_test(self):
                n_list = [-100, 200, 400]
                self.assertEqual(max_integer(n_list), 400)

        def third_test(self):
                n_list = [1]
                self.assertEqual(max_integer(n_list), 1)

        def four_test(self):
                n_list = []
                self.assertEqual(max_integer(n_list), None)

        def five_test(self):
                n_list = [20.4, 34.5, 38.7]
                self.assertEqual(max_integer(n_list), 38.7)

        def six_test(self):
                n_list = [20.4, 'm', 38.7]
                with self.assertRaises(TypeError):
                        max_integer(n_list)

        def seven_test(self):
                n_list = ['j', 22, 38.7]
                with self.assertRaises(TypeError):
                        max_integer(n_list)

        def eight_test(self):
                n_list = [-34, -22, 0]
                self.assertEqual(max_integer(n_list), 0)

        def nine_test(self):
                n_list = "oz"
                self.assertEqual(max_integer(n_list), 'z')

if __name__ == '__main__':
    unittest.main()
