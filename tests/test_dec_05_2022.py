import unittest
from advent_of_code_2022 import dec_05_2022

example_data = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    "1   2   3",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]


class TestCrateStacker(unittest.TestCase):
    def test_example_init(self):
        expected_stacks = [["N", "Z"], ["D", "C", "M"], ["P"]]
        expected_instructions = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
        crate_stacker = dec_05_2022.CrateStacker(example_data)
        self.assertEqual(crate_stacker.crate_lines, example_data[:3])
        self.assertEqual(crate_stacker.move_instruction_lines, example_data[5:])
        self.assertEqual(crate_stacker.crate_stacks, expected_stacks)
        self.assertEqual(crate_stacker.move_instructions, expected_instructions)

        crate_stacker.consume_instructions()
        post_expected_stacks = [["C"], ["M"], ["Z", "N", "D", "P"]]
        self.assertEqual(crate_stacker.crate_stacks, post_expected_stacks)

        self.assertEqual(crate_stacker.top_contents(), "CMZ")

        crate_stacker.set_stacks()
        self.assertEqual(crate_stacker.crate_stacks, expected_stacks)

        crate_stacker.consume_instructions(9001)
        post_9001_stacks = [["M"], ["C"], ["D", "N", "Z", "P"]]
        self.assertEqual(crate_stacker.crate_stacks, post_9001_stacks)
        self.assertEqual(crate_stacker.top_contents(), "MCD")
