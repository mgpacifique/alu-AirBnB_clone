#!/usr/bin/python3
"""
Unit tests for models/city.py
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_instantiation(self):
        """Test if a new City instance is correctly created"""
        c = City()
        self.assertIsInstance(c, City)
        self.assertTrue(hasattr(c, "id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))

    def test_attributes(self):
        """Test if City correctly inherits Base attributes and has its own"""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertEqual(c.state_id, "")
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.name, "")


if __name__ == '__main__':
    unittest.main()
