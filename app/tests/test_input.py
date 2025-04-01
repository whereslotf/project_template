import unittest
import os
import tempfile
from input import read_file_builtin, read_file_pandas


class TestReadFileBuiltin(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8")
        self.temp_file.write("Hello, World!")
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_read_file_builtin_success(self):
        content = read_file_builtin(self.temp_file.name)
        self.assertEqual(content, "Hello, World!")

    def test_read_file_builtin_file_not_found(self):
        content = read_file_builtin("nonexistent_file.txt")
        self.assertIn("Error reading file", content)

    def test_read_file_builtin_empty_file(self):
        empty_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8")
        empty_file.close()
        content = read_file_builtin(empty_file.name)
        self.assertEqual(content, "")
        os.remove(empty_file.name)

if __name__ == "__main__":
    unittest.main()
