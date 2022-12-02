import unittest
from advent_of_code_2022 import dec_02_2022

test_data = """
A Y
B X
C Z
"""


class TestDecoder1(unittest.TestCase):
    """Unit tests for decoder_1 function"""
    def test_example(self):
        """Tests if provided example is correctly decoded"""
        expected_value = [[1, 2], [2, 1], [3, 3]]
        self.assertEqual(dec_02_2022.decoder_1(test_data), expected_value)


class TestDecoder2(unittest.TestCase):
    """Unit tests for decoder_2 function"""
    def test_example(self):
        """Tests if provided example is correctly decoded"""
        expected_value = [[1, 1], [2, 1], [3, 1]]
        self.assertEqual(dec_02_2022.decoder_2(test_data), expected_value)


class TestRoundScore(unittest.TestCase):
    """Unit tests for round score calculator"""

    def test_draw(self):
        """Tests if draw outcomes are calculated correctly"""
        self.assertEqual(dec_02_2022.round_score(1, 1), 4)
        self.assertEqual(dec_02_2022.round_score(2, 2), 5)
        self.assertEqual(dec_02_2022.round_score(3, 3), 6)

    def test_loss(self):
        """Tests if loss outcomes are calculated correctly"""
        self.assertEqual(dec_02_2022.round_score(1, 3), 3)
        self.assertEqual(dec_02_2022.round_score(2, 1), 1)
        self.assertEqual(dec_02_2022.round_score(3, 2), 2)

    def test_win(self):
        """Tests if win outcomes are calculated correctly"""
        self.assertEqual(dec_02_2022.round_score(3, 1), 7)
        self.assertEqual(dec_02_2022.round_score(1, 2), 8)
        self.assertEqual(dec_02_2022.round_score(2, 3), 9)


class TestTotalScore(unittest.TestCase):
    """Unit tests for total score calculator"""

    def test_example(self):
        """Tests if provided example is correctly replicated"""
        decoded_data = dec_02_2022.decoder_1(test_data)
        self.assertEqual(dec_02_2022.total_score(decoded_data), 15)
