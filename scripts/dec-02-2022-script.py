# -*- coding: utf-8 -*-

"""dec-02-2022-script.py

This script accepts a text file representing a rock, paper, scissors tournament strategy guide and outputs:
  - The total score obtained by following the guide using code 1
  - The total score obtained by following the guide using code 2

Example:
    $ dec-02-2022-script.py strategy_guide.txt
"""

from advent_of_code_2022 import dec_02_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('strategy_guide',
                            help="text file with tournament strategy guide")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    text_data = utils.load_txt_data(args.strategy_guide)

    decoded_data_1 = dec_02_2022.decoder_1(text_data)
    total_score_1 = dec_02_2022.total_score(decoded_data_1)

    decoded_data_2 = dec_02_2022.decoder_2(text_data)
    total_score_2 = dec_02_2022.total_score(decoded_data_2)

    print(f'Total score assuming code 1: {total_score_1}')
    print(f'Total score assuming code 2: {total_score_2}')
