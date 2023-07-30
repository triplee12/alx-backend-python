#!/usr/bin/env python3
"""Parameterize a unit test."""

import requests
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from .utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, result):
        """Test access nested map."""
        self.assertEqual(access_nested_map(nested_map, path), result)
