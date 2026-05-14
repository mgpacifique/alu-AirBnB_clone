#!/usr/bin/python3
"""
Unit tests for models/place.py
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_instantiation(self):
        """Test if a new Place instance is correctly created"""
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertTrue(hasattr(p, "id"))
        self.assertTrue(hasattr(p, "created_at"))
        self.assertTrue(hasattr(p, "updated_at"))

    def test_attributes(self):
        """Test if Place correctly inherits Base attributes and has its own"""
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertEqual(p.city_id, "")
        self.assertTrue(hasattr(p, "user_id"))
        self.assertEqual(p.user_id, "")
        self.assertTrue(hasattr(p, "name"))
        self.assertEqual(p.name, "")
        self.assertTrue(hasattr(p, "description"))
        self.assertEqual(p.description, "")
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertEqual(p.number_rooms, 0)
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertEqual(p.number_bathrooms, 0)
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertEqual(p.max_guest, 0)
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertEqual(p.price_by_night, 0)
        self.assertTrue(hasattr(p, "latitude"))
        self.assertEqual(p.latitude, 0.0)
        self.assertTrue(hasattr(p, "longitude"))
        self.assertEqual(p.longitude, 0.0)
        self.assertTrue(hasattr(p, "amenity_ids"))
        self.assertEqual(p.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
