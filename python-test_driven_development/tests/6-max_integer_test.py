#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_empty_list(self):
        """Empty list should return None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Default argument should behave like empty list"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Single element list returns that element"""
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        """Sorted list returns last element"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Unsorted list returns max element"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Works with all negative numbers"""
        self.assertEqual(max_integer([-10, -5, -7]), -5)

    def test_mixed_sign_numbers(self):
        """Works with negative and positive numbers"""
        self.assertEqual(max_integer([-10, 0, 5, 2]), 5)

    def test_repeated_max(self):
        """Works when max value appears multiple times"""
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_floats(self):
        """Works with floats (comparison still valid)"""
        self.assertEqual(max_integer([1.2, 3.4, 2.2]), 3.4)

    def test_strings(self):
        """Works with strings (lexicographic max)"""
        self.assertEqual(max_integer(["a", "z", "b"]), "z")


if __name__ == "__main__":
    unittest.main()
