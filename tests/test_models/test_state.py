#!/usr/bin/python3
"""
Unit tests for models/state.py
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_instantiation(self):
        """Test if a new State instance is correctly created"""
        s = State()
        self.assertIsInstance(s, State)
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))

    def test_attributes(self):
        """Test if State correctly inherits Base attributes and has its own"""
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")


if __name__ == '__main__':
    unittest.main()
