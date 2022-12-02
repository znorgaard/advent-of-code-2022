# -*- coding: utf-8 -*-

"""dec-01-2022-script.py

This script accepts a text file of elf calorie counts as input and outputs:
  - the maximum calorie count for a single elf
  - the total calories carried by the top three elves

Example:
    $ dec-01-2022-script.py calories.txt
"""

from advent_of_code_2022 import dec_01_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('calorie_file',
                            help="text file with elf calorie counts")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    text_data = utils.load_txt_data(args.calorie_file)

    max_calories = dec_01_2022.max_calories(text_data)
    top_3_calories = dec_01_2022.top_n_elves(text_data, 3)

    print(f'Max single elf calories: {max_calories}')
    print(f'Top 3 elves total calories: {top_3_calories}')



