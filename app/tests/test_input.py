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

class TestReadFilePandas(unittest.TestCase):
    def setUp(self):
        self.temp_csv = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv", encoding="utf-8")
        self.temp_csv.write("col1,col2\nvalue1,value2")
        self.temp_csv.close()

    def tearDown(self):
        os.remove(self.temp_csv.name)

    def test_read_file_pandas_success(self):
        content = read_file_pandas(self.temp_csv.name)
        self.assertIn("col1", content)
        self.assertIn("value1", content)

    def test_read_file_pandas_file_not_found(self):
        content = read_file_pandas("nonexistent_file.csv")
        self.assertIn("Error reading file with pandas", content)

    def test_read_file_pandas_empty_file(self):
        empty_csv = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv", encoding="utf-8")
        empty_csv.close()
        content = read_file_pandas(empty_csv.name)
        self.assertIn("Error reading file with pandas", content)
        os.remove(empty_csv.name)

if __name__ == "__main__":
    unittest.main()

