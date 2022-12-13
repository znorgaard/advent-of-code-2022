import unittest
from advent_of_code_2022 import dec_06_2022


class TestFindStart(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(dec_06_2022.find_unique("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(dec_06_2022.find_unique("nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(dec_06_2022.find_unique("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(dec_06_2022.find_unique("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)
        self.assertEqual(dec_06_2022.find_unique("AAAA"), -1)

        self.assertEqual(dec_06_2022.find_unique("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
        self.assertEqual(dec_06_2022.find_unique("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(dec_06_2022.find_unique("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(dec_06_2022.find_unique("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(dec_06_2022.find_unique("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)
