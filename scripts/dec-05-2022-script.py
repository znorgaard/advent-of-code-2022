# -*- coding: utf-8 -*-

"""dec-05-2022-script.py

This script accepts a text file representing a stack of crates and crate moving instructions and outputs:
  - A string representing the contents of the top crate in each stack after crate stacker 9000 moving instructions
  - A string representing the contents of the top crate in each stack after crate stacker 9001 moving instructions

Example:
    $ dec-05-2022-script.py crate_doc.txt
"""

from advent_of_code_2022 import dec_05_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('puzzle_input',
                            help="text file with puzzle input")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    list_data = utils.lines_to_list(utils.load_txt_data(args.puzzle_input))
    crateStacker = dec_05_2022.CrateStacker(list_data)
    crateStacker.consume_instructions()

    print(f'After following 9000 instructions, the top contents are: {crateStacker.top_contents()}')

    crateStacker.set_stacks()
    crateStacker.consume_instructions(9001)
    print(f'After following 9001 instructions, the top contents are: {crateStacker.top_contents()}')
