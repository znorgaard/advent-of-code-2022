import unittest
from advent_of_code_2022 import dec_01_2022

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


class TestMaxCalories(unittest.TestCase):
    """Unit tests for max calorie counter"""

    def test_example(self):
        """Tests if provided example is correctly replicated"""
        self.assertEqual(dec_01_2022.max_calories(test_data), 24000)


class TestTopNElves(unittest.TestCase):
    """Unit tests for top n elves calorie total"""

    def test_example(self):
        """Tests if provided example is correctly replicated"""
        self.assertEqual(dec_01_2022.top_n_elves(test_data, 3), 45000)


class TestPerElfCalories(unittest.TestCase):
    """Unit tests for per elf calorie calculator"""

    def test_example(self):
        """Tests if provided example is correctly replicated"""
        expected_calories = [6000, 4000, 11000, 24000, 10000]
        self.assertEqual(dec_01_2022.calories_by_elf(test_data), expected_calories)
