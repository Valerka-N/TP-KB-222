import unittest
import io
import os
import csv
from unittest.mock import patch
from lab2 import *

class TestLab2Script(unittest.TestCase):
    def setUp(self):
        self.test_file = "lab2.csv"
        self.test_data = [
            {"name": "John", "phone": "9675643454", "specialty": "21", "group": "12"},
            {"name": "Alice", "phone": "734586290", "specialty": "19", "group": "22"},
        ]

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_add(self):
        with open(self.test_file, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "specialty", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.test_data)

        slist = []
        updated_list = add(self.test_file, slist)
        self.assertEqual(updated_list, self.test_data)

    def test_save(self):
        slist = self.test_data
        save(self.test_file, slist)
        self.assertTrue(os.path.exists(self.test_file))

    def test_printAllList(self):
        slist = self.test_data
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(slist)
            output = mock_stdout.getvalue()
            self.assertIn("John", output)
            self.assertIn("Alice", output)

    def test_addNewElement(self):
        slist = self.test_data
        with patch('builtins.input', side_effect=["New Student", "9675643454", "22", "14"]):
            addNewElement(slist)
            self.assertEqual(len(slist), 3)

    def test_deleteElement(self):
        slist = self.test_data
        with patch('builtins.input', return_value="Alice"):
            deleteElement(slist)
            self.assertEqual(len(slist), 1)

    def test_updateElement(self):
        slist = self.test_data
        with patch('builtins.input', side_effect=["Alice", "New Alice", "734586290", "26", "45"]):
            updateElement(slist)
            self.assertEqual(slist[0]["name"], "John")


if __name__ == '__main__':
    unittest.main()