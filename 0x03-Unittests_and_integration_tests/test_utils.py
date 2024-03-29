#!/usr/bin/env python3
"""Unittests for the utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class to test access nested map"""
    @parameterized.expand(
        [({"a": 1}, ("a",), 1),
         ({"a": {"b": 2}}, ("a",), {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2), ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """Test access nested map function with exceptions"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get json class"""
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
    """Tests the memoize function."""

    def test_memoize(self):
        """Tests memoize's output."""
        class TestClass:
            """Test class for a_method, a_property"""
            def a_method(self):
                """a_method function"""
                return 42

            @memoize
            def a_property(self):
                """a_property function"""
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


if __name__ == "__main__":
    unittest.main()
