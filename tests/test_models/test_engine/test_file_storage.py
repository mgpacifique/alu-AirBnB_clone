#!/usr/bin/python3
"""
Unit tests for models/engine/file_storage.py
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        # Access the private file path attribute for cleanups
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove(self.file_path)
        except Exception:
            pass

    def test_all_returns_dict(self):
        """Test if all() returns a dictionary"""
        obj_dict = self.storage.all()
        self.assertEqual(type(obj_dict), dict)

    def test_new(self):
        """Test if new() adds an object to __objects"""
        b = BaseModel()
        self.storage.new(b)
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Test if objects are properly saved to JSON and reloaded"""
        b1 = BaseModel()
        self.storage.new(b1)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        # Empty the storage to test reloading
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(b1.__class__.__name__, b1.id)
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
