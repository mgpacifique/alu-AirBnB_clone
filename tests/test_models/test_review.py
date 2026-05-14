#!/usr/bin/python3
"""
Unit tests for models/review.py
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instantiation(self):
        """Test if a new Review instance is correctly created"""
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))

    def test_attributes(self):
        """Test if Review correctly inherits Base attributes and has its own"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertEqual(r.place_id, "")
        self.assertTrue(hasattr(r, "user_id"))
        self.assertEqual(r.user_id, "")
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.text, "")


if __name__ == '__main__':
    unittest.main()
