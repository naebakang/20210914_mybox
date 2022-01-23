# File encoding: UTF-8

import unittest
from algorithm import array


class TestArray(unittest.TestCase):
    """
    Test that the result sum of all numbers
    """
    def setUp(self):
        self.array = array.Array('1 2 3 4 10 11')

    def test_sum(self):
        result = self.array.sum(6)
        self.assertEqual(result, 31)

    def test_sum_raise_exception(self):
        self.assertRaises(Exception, lambda: array.Array().sum(5, '1 2 3 4 10 11'))

    def tearDown(self):
        print('element = {}'.format(self.array))
