# -*- coding: utf-8 -*-

"""dec-03-2022-script.py

This script accepts a text file representing the contents of many elf rucksacks and ouputs:
  - The sum of the priority of items sorted improperly (same item type in multiple compartments)
  - The sum of the priority of each group's badge

Example:
    $ dec-03-2022-script.py rucksack_contents.txt
"""

from advent_of_code_2022 import dec_03_2022, utils
import argparse


def parse_args():
    """Parse arguments from the command-line."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('rucksack_contents',
                            help="text file with rucksack contents")
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    list_data = utils.lines_to_list(utils.load_txt_data(args.rucksack_contents))

    split_rucksacks = [dec_03_2022.divide_rucksack(rucksack_string) for rucksack_string in list_data]
    shared_items = [dec_03_2022.shared_items(compartments) for compartments in split_rucksacks]

    priorities = [dec_03_2022.get_priorities(items, dec_03_2022.letter_order) for items in shared_items]
    priority_sum = sum(sum(priorities, []))  # first sum flattens list

    grouped_data = dec_03_2022.make_groups(list_data)
    group_badges = [dec_03_2022.shared_items(group) for group in grouped_data]
    group_priorities = [dec_03_2022.get_priorities(items, dec_03_2022.letter_order) for items in group_badges]
    badge_sum = sum(sum(group_priorities, []))

    print(f'Sum of priorities of items stored improperly: {priority_sum}')
    print(f'Sum of priorities of group badges: {badge_sum}')
