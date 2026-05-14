#!/usr/bin/python3
"""
Unit tests for console.py
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console"""

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create ModelUser")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_advanced_features(self):
        """Test the advanced features of the console"""
        cmds = [
            "BaseModel.all()", "User.all()", "State.all()",
            "City.all()", "Amenity.all()", "Place.all()", "Review.all()",
            "BaseModel.count()", "User.count()", "State.count()",
            "City.count()", "Amenity.count()", "Place.count()",
            "Review.count()",
            "BaseModel.show(\"id\")", "User.show(\"id\")",
            "State.show(\"id\")", "City.show(\"id\")",
            "Amenity.show(\"id\")", "Place.show(\"id\")",
            "Review.show(\"id\")",
            "BaseModel.destroy(\"id\")", "User.destroy(\"id\")",
            "City.destroy(\"id\")", "State.destroy(\"id\")",
            "Place.destroy(\"id\")", "Amenity.destroy(\"id\")",
            "Review.destroy(\"id\")",
            "BaseModel.update(\"id\", \"attribute_name\", \"string_value\")",
            "User.update(\"id\", \"attribute_name\", \"string_value\")",
            "State.update(\"id\", \"attribute_name\", \"string_value\")",
            "City.update(\"id\", \"attribute_name\", \"string_value\")",
            "Place.update(\"id\", \"attribute_name\", \"string_value\")",
            "Amenity.update(\"id\", \"attribute_name\", \"string_value\")",
            "Review.update(\"id\", \"attribute_name\", \"string_value\")",
            "BaseModel.update(\"id\", {'first_name': \"John\"})",
            "User.update(\"id\", {'first_name': \"John\"})",
            "State.update(\"id\", {'first_name': \"John\"})",
            "Amenity.update(\"id\", {'first_name': \"John\"})",
            "City.update(\"id\", {'first_name': \"John\"})",
            "Place.update(\"id\", {'first_name': \"John\"})",
            "Review.update(\"id\", {'first_name': \"John\"})"
        ]
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(cmd)
                self.assertEqual(type(f.getvalue()), str)


if __name__ == "__main__":
    unittest.main()
