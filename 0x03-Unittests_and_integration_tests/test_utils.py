#!/usr/bin/env python3
"""Unittests for the utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        [({"a": 1}, ("a",), 1),
         ({"a": {"b": 2}}, ("a",), {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2), ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Create a Mock object with json method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        """Mock the requests.get method"""
        with patch('requests.get', return_value=mock_response) as mock_get:
            """Call the get_json method"""
            result = get_json(test_url)
            """Assert that requests.get was called once with test_url"""
            mock_get.assert_called_once_with(test_url)
            """Assert that the result of get_json is equal to test_payload"""
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """Create an instance of TestClass"""
        test_instance = self.TestClass()
        result1 = test_instance.a_property
        result2 = test_instance.a_property
        mock_a_method.assert_called_once()
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
