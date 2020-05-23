#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        """ Class of testing """

        def test_first_test(self):
                n_list = [100, 200, 400]
                self.assertEqual(max_integer(n_list), 400)

        def test_second_test(self):
                n_list = [-100, 200, 400]
                self.assertEqual(max_integer(n_list), 400)

        def test_third_test(self):
                n_list = [1]
                self.assertEqual(max_integer(n_list), 1)

        def test_four_test(self):
                n_list = []
                self.assertEqual(max_integer(n_list), None)

        def test_five_test(self):
                n_list = [20.4, 34.5, 38.7]
                self.assertEqual(max_integer(n_list), 38.7)

        def test_six_test(self):
                n_list = [20.4, 'm', 38.7]
                with self.assertRaises(TypeError):
                        max_integer(n_list)

        def test_seven_test(self):
                n_list = ['j', 22, 38.7]
                with self.assertRaises(TypeError):
                        max_integer(n_list)

        def test_eight_test(self):
                n_list = [-34, -22, 0]
                self.assertEqual(max_integer(n_list), 0)

        def test_nine_test(self):
                n_list = "oz"
                self.assertEqual(max_integer(n_list), 'z')

if __name__ == '__main__':
    unittest.main()
