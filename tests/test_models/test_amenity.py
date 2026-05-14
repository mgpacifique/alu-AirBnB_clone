#!/usr/bin/python3
"""
Unit tests for models/amenity.py
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_instantiation(self):
        """Test if a new Amenity instance is correctly created"""
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))

    def test_attributes(self):
        """Test if Amenity inherits Base attributes and has its own"""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")


if __name__ == '__main__':
    unittest.main()
