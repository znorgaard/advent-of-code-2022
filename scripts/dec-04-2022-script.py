# -*- coding: utf-8 -*-

"""dec-04-2022-script.py

This script accepts a text file representing elf section cleaning assignments and outputs:
  - The number of elf pairs where one cleaning assignment fully overlaps the other
  - The number of elf pairs with any cleaning assignment overlaps

Example:
    $ dec-04-2022-script.py cleaning_assignments.txt
"""

from advent_of_code_2022 import dec_04_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('cleaning_assignments',
                            help="text file with cleaning assignments")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    list_data = utils.lines_to_list(utils.load_txt_data(args.cleaning_assignments))
    cleaning_ranges = [dec_04_2022.make_ranges(cleaning_pair) for cleaning_pair in list_data]
    full_overlap = sum([dec_04_2022.check_full_overlap(range1, range2) for (range1, range2) in cleaning_ranges])
    overlaps = sum([dec_04_2022.check_overlap(range1, range2) for (range1, range2) in cleaning_ranges])

    print(f'Fully overlapping cleaning pairs: {full_overlap}')
    print(f'Overlapping cleaning pairs: {overlaps}')
