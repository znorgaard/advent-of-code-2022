import unittest
from advent_of_code_2022 import dec_03_2022

example_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


class TestMakeGroups(unittest.TestCase):
    def test_example(self):
        expected_data = [
            ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],
            ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        ]
        self.assertEqual(dec_03_2022.make_groups(example_data), expected_data)


class TestDivideRucksack(unittest.TestCase):
    def test_example(self):
        expected_data = [
            ["vJrwpWtwJgWr", "hcsFMMfFFhFp"],
            ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"],
            ["PmmdzqPrV", "vPwwTWBwg"],
            ["wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"],
            ["ttgJtRGJ", "QctTZtZT"],
            ["CrZsJsPPZsGz", "wwsLwLmpwMDw"],
        ]
        self.assertEqual(
            [dec_03_2022.divide_rucksack(rucksack_string) for rucksack_string in example_data],
            expected_data
        )


class TestSharedItems(unittest.TestCase):
    def test_example(self):
        expected_data = [{"p"}, {"L"}, {"P"}, {"v"}, {"t"}, {"s"}]
        split_rucksacks = [dec_03_2022.divide_rucksack(rucksack_string) for rucksack_string in example_data]
        self.assertEqual([dec_03_2022.shared_items(compartments) for compartments in split_rucksacks], expected_data)

        groups = [
            ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],
            ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
        ]

        self.assertEqual([dec_03_2022.shared_items(group) for group in groups], [{"r"}, {"Z"}])


class TestGetPriorities(unittest.TestCase):
    def test_example(self):
        input_data = [{"p"}, {"L"}, {"P"}, {"v"}, {"t"}, {"s"}]
        output_data = [dec_03_2022.get_priorities(items, dec_03_2022.letter_order) for items in input_data]
        expected_data = [[16], [38], [42], [22], [20], [19]]

        self.assertEqual(output_data, expected_data)
        self.assertEqual(sum(sum(output_data, [])), 157)  # first sum with empty list flattens list

        input_group_data = [{"r"}, {"Z"}]
        output_group_data = [dec_03_2022.get_priorities(items, dec_03_2022.letter_order) for items in input_group_data]
        expected_group_data = [[18], [52]]

        self.assertEqual(output_group_data, expected_group_data)
        self.assertEqual(sum(sum(output_group_data, [])), 70)  # first sum with empty list flattens list
