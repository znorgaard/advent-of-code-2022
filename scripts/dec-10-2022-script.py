# -*- coding: utf-8 -*-

"""dec-10-2022-script.py

This script accepts a text file representing program instructions for an elf communicator:
  - the sum of the signal strength at the 20th cycle and every 40th cycle after that
  - the message!

Example:
    $ dec-10-2022-script.py instructions.txt
"""

from advent_of_code_2022 import dec_10_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('puzzle_input',
                            help="text file with puzzle input")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    instructions = utils.lines_to_list(utils.load_txt_data("./input_data/dec-10-2022.txt").strip())
    communicator = dec_10_2022.Communicator()

    for instruction in instructions:
        communicator.follow_instructions(instruction)

    print(f'Sum of signal strength at 20th and every 40th cycle afterwards: {communicator.sum_interesting_cycles()}')
    print(f'{communicator.get_image()}')
