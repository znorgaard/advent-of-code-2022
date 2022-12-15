import unittest
import numpy as np
from numpy import testing
from advent_of_code_2022 import dec_08_2022

example_data = np.array([
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
])


class TestCheckVisibility(unittest.TestCase):
    def test_example(self):
        expected_column_visibility = np.array([
            [True,  True,  True,  True,  True],
            [False, True,  True,  False, False],
            [True,  False, False, False, False],
            [False, False, True,  False, True],
            [True,  True,  True,  True,  True]
        ])
        expected_row_visibility = np.array([
            [True, False, False, True,  True],
            [True, True,  True,  False, True],
            [True, True,  False, True,  True],
            [True, False, True,  False, True],
            [True, True,  False, True,  True]
        ])
        expected_mat_visibility = np.array([
            [True, True,  True,  True,  True],
            [True, True,  True,  False, True],
            [True, True,  False, True,  True],
            [True, False, True,  False, True],
            [True, True,  True,  True,  True]
        ])
        testing.assert_array_equal(
            np.apply_along_axis(dec_08_2022.bidirectional_visibility, 0, example_data),
            expected_column_visibility
        )
        testing.assert_array_equal(
            np.apply_along_axis(dec_08_2022.bidirectional_visibility, 1, example_data),
            expected_row_visibility
        )

        visibility_matrix = dec_08_2022.matrix_visibility(example_data)
        testing.assert_array_equal(
            visibility_matrix,
            expected_mat_visibility
        )

        self.assertEqual(np.sum(visibility_matrix), 21)


class CheckScenicScores(unittest.TestCase):
    def test_example(self):
        expected_forward_row_scores = np.array([
            [0, 1, 2, 3, 1],
            [0, 1, 1, 1, 2],
            [0, 1, 1, 1, 1],
            [0, 1, 2, 1, 4],
            [0, 1, 1, 3, 1]
        ])
        expected_row_scores = np.array([
            [0, 1, 2, 3, 0],
            [0, 1, 2, 1, 0],
            [0, 3, 1, 1, 0],
            [0, 1, 4, 1, 0],
            [0, 2, 1, 3, 0]
        ])
        expected_column_scores = np.array([
            [0, 0, 0, 0, 0],
            [1, 1, 2, 1, 1],
            [4, 2, 1, 2, 1],
            [1, 1, 2, 3, 3],
            [0, 0, 0, 0, 0]
        ])
        expected_scores = np.array([
            [0, 0, 0, 0, 0],
            [0, 1, 4, 1, 0],
            [0, 6, 1, 2, 0],
            [0, 1, 8, 3, 0],
            [0, 0, 0, 0, 0]
        ])
        testing.assert_array_equal(
            np.apply_along_axis(dec_08_2022.scenic_scores, 1, example_data),
            expected_forward_row_scores
        )
        testing.assert_array_equal(
            np.apply_along_axis(dec_08_2022.bidirectional_scenic_scores, 1, example_data),
            expected_row_scores
        )
        testing.assert_array_equal(
            np.apply_along_axis(dec_08_2022.bidirectional_scenic_scores, 0, example_data),
            expected_column_scores
        )
        scenic_matrix = dec_08_2022.matrix_scenic(example_data)
        testing.assert_array_equal(scenic_matrix, expected_scores)
        self.assertEqual(scenic_matrix.max(), 8)
