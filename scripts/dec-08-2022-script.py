# -*- coding: utf-8 -*-

"""dec-08-2022-script.py

This script accepts a text file representing a tree height matrix and returns:
  - the number of trees visible from the outer edges
  - the maximum scenic score for a tree in the forest

Example:
    $ dec-08-2022-script.py tree_heights.txt
"""

from advent_of_code_2022 import dec_08_2022, utils
import numpy as np
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('puzzle_input',
                            help="text file with puzzle input")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    tree_height_strings = utils.lines_to_list(utils.load_txt_data(args.puzzle_input).strip())
    height_matrix = np.array([[int(h) for h in list(heights)] for heights in tree_height_strings])
    visibility_matrix = dec_08_2022.matrix_visibility(height_matrix)

    print(f'visible tree count: {np.sum(visibility_matrix)}')

    scenic_matrix = dec_08_2022.matrix_scenic(height_matrix)
    print(f'max scenic score: {scenic_matrix.max()}')
