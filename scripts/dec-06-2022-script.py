# -*- coding: utf-8 -*-

"""dec-06-2022-script.py

This script accepts a text file representing a data stream and outputs:
  - the end position of the start-of-packet marker
  - the end position of the start-of-message marker

Example:
    $ dec-06-2022-script.py datastream.txt
"""

from advent_of_code_2022 import dec_06_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('puzzle_input',
                            help="text file with puzzle input")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    datastream = utils.load_txt_data(args.puzzle_input).strip()

    print(f'start-of-packet marker ends: {dec_06_2022.find_unique(datastream)}')
    print(f'start-of-message marker ends: {dec_06_2022.find_unique(datastream, 14)}')
