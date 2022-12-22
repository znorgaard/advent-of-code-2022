import unittest
from advent_of_code_2022 import utils, dec_10_2022

short_example = ["noop", "addx 3", "addx -5"]

long_example = utils.lines_to_list("""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""")

expected_image = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""


class TestCommunicator(unittest.TestCase):
    def test_short_example(self):
        communicator = dec_10_2022.Communicator()
        for instruction in short_example:
            communicator.follow_instructions(instruction)
        self.assertEqual(communicator.cycle, 5)
        self.assertEqual(communicator.x, -1)
        self.assertEqual(communicator.interesting_cycles, [])

    def test_long_example(self):
        expected_interesting_cycles = [(20, 420), (60, 1140), (100, 1800), (140, 2940), (180, 2880), (220, 3960)]

        long_communicator = dec_10_2022.Communicator()
        for instruction in long_example:
            long_communicator.follow_instructions(instruction)
        self.assertEqual(long_communicator.interesting_cycles, expected_interesting_cycles)
        self.assertEqual(long_communicator.sum_interesting_cycles(), 13140)

        print(f'{long_communicator.get_image()}')

        self.assertEqual(long_communicator.get_image(), expected_image)
