#!/usr/bin/python3
"""
Unit tests for models/user.py
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_instantiation(self):
        """Test if a new User instance is correctly created"""
        u = User()
        self.assertIsInstance(u, User)
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_attributes(self):
        """Test if User correctly inherits Base attributes and has its own"""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertEqual(u.email, "")
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.password, "")
        self.assertTrue(hasattr(u, "first_name"))
        self.assertEqual(u.first_name, "")
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.last_name, "")


if __name__ == '__main__':
    unittest.main()
