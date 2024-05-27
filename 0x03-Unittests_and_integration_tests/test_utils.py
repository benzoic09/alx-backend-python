#!/usr/bin/env python3
"""unittest"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class to test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_acess_nested_map(self, nested_map, path, expected):
        """ test that access_nested_map returns
        the expected results"""
        self.assertEqual(access_nested_map(
            nested_map, path), expected)
