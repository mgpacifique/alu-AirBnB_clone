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


if __name__ == "__main__":
    unittest.main()
