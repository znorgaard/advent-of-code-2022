import unittest
import tempfile
import os
from advent_of_code_2022 import utils

test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


class TestLoadData(unittest.TestCase):
    """Tests if text files are read correctly"""

    def test_example(self):
        with tempfile.TemporaryDirectory() as tempdir:
            temp_file_path = os.path.join(tempdir, 'test_data.txt')
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(test_data)

            self.assertEqual(utils.load_txt_data(temp_file_path), test_data)

class TestLinesToList(unittest.TestCase):
    """Tests if multiline strings are split correctly"""

    def test_example(self):
        expected_list = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]
        self.assertEqual(utils.lines_to_list(test_data), expected_list)
