# -*- coding: utf-8 -*-

"""dec-09-2022-script.py

This script accepts a text file representing the directions to move the head of a rope:
  - the number of unique positions visited by a 2 knot rope tail
  - the number of unique positions visited by a 10 knot rope tail

Example:
    $ dec-09-2022-script.py rope_movements.txt
"""

from advent_of_code_2022 import dec_09_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('puzzle_input',
                            help="text file with puzzle input")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    commands = [
        (direction, int(distance)) for direction, distance in
        [command.split(" ") for command in utils.lines_to_list(utils.load_txt_data("./input_data/dec-09-2022.txt").strip())]
    ]
    rope = dec_09_2022.LongRope(2)

    for direction, distance in commands:
        rope.move_head(direction, distance)

    print(f'tail positions visited: {len(rope.tail_positions)}')

    long_rope = dec_09_2022.LongRope(10)

    for direction, distance in commands:
        long_rope.move_head(direction, distance)

    print(f'tail positions visited with long_rope: {len(long_rope.tail_positions)}')
