import unittest
from advent_of_code_2022 import dec_04_2022

example_data = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]
expected_ranges = [
    [range(2, 5), range(6, 9)],
    [range(2, 4), range(4, 6)],
    [range(5, 8), range(7, 10)],
    [range(2, 9), range(3, 8)],
    [range(6, 7), range(4, 7)],
    [range(2, 7), range(4, 9)],
]


class TestMakeRanges(unittest.TestCase):
    def test_example(self):
        self.assertEqual([dec_04_2022.make_ranges(range_string) for range_string in example_data], expected_ranges)


class TestCheckFullOverlap(unittest.TestCase):
    def test_example(self):
        expected_data = [False, False, False, True, True, False]
        output_data = [dec_04_2022.check_full_overlap(range1, range2) for (range1, range2) in expected_ranges]
        self.assertEqual(output_data, expected_data)

        self.assertEqual(sum(output_data), 2)


class TestCheckOverlap(unittest.TestCase):
    def test_example(self):
        expected_data = [False, False, True, True, True, True]
        output_data = [dec_04_2022.check_overlap(range1, range2) for (range1, range2) in expected_ranges]
        self.assertEqual(output_data, expected_data)

        self.assertEqual(sum(output_data), 4)
