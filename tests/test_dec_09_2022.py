import unittest
from advent_of_code_2022 import dec_09_2022

example_data = [
    ("R", 4),
    ("U", 4),
    ("L", 3),
    ("D", 1),
    ("R", 4),
    ("D", 1),
    ("L", 5),
    ("R", 2),
]

long_example = [
    ("R", 5),
    ("U", 8),
    ("L", 8),
    ("D", 3),
    ("R", 17),
    ("D", 10),
    ("L", 25),
    ("U", 20),
]


class TestLongRope(unittest.TestCase):
    def test_example(self):
        rope = dec_09_2022.LongRope(2)
        for direction, distance in example_data:
            rope.move_head(direction, distance)
        self.assertEqual(len(rope.tail_positions), 13)

        long_rope = dec_09_2022.LongRope(10)
        for direction, distance in example_data:
            long_rope.move_head(direction, distance)
        self.assertEqual(len(long_rope.tail_positions), 1)

        long_rope_2 = dec_09_2022.LongRope(10)
        for direction, distance in long_example:
            long_rope_2.move_head(direction, distance)
        self.assertEqual(len(long_rope_2.tail_positions), 36)
