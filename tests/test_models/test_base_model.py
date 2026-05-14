#!/usr/bin/python3
"""
Unit tests for models/base_model.py
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instantiation(self):
        """Test if a new instance is correctly created"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_str(self):
        """Test the string representation of BaseModel"""
        b = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(str(b), expected_str)

    def test_save(self):
        """Test if save updates the updated_at attribute"""
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(b.updated_at, old_updated_at)
        self.assertGreater(b.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test if to_dict returns a correct dictionary"""
        b = BaseModel()
        b_dict = b.to_dict()

        self.assertIsInstance(b_dict, dict)
        self.assertEqual(b_dict['__class__'], 'BaseModel')
        self.assertEqual(b_dict['id'], b.id)
        self.assertIsInstance(b_dict['created_at'], str)
        self.assertIsInstance(b_dict['updated_at'], str)

    def test_kwargs_instantiation(self):
        """Test creating an instance from a dictionary"""
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)

        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        # Values match, but they are different objects in memory
        self.assertNotEqual(b1, b2)


if __name__ == '__main__':
    unittest.main()
