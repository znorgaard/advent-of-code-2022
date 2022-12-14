# -*- coding: utf-8 -*-

"""dec-07-2022-script.py

This script accepts a text file representing a series of terminal inputs+outputs and returns:
  - the total size of all directories with a size <= 100000
  - size of the smallest directory to delete to make available space >= 30000000

Example:
    $ dec-07-2022-script.py terminal.txt
"""

from advent_of_code_2022 import dec_07_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('puzzle_input',
                            help="text file with puzzle input")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    terminal_lines = utils.lines_to_list(utils.load_txt_data(args.puzzle_input).strip())

    dir_tree = dec_07_2022.build_tree(terminal_lines)
    big_dir_size_total = sum([size for dir_name, size in dir_tree.dir_sizes().items() if size <= 100000])

    print(f'total size of all directories with a size <= 100000: {big_dir_size_total}')

    min_delete = 30000000 - (70000000 - dir_tree.get_size())
    to_delete = min([val for val in dir_tree.dir_sizes().values() if val >= min_delete])
    print(f'smallest directory size to delete to make available space >= 30000000: {to_delete}')
