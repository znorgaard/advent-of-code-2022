# -*- coding: utf-8 -*-

"""
Puzzle prompts are getting long, go see it here:
https://adventofcode.com/2022/day/9
https://adventofcode.com/2022/day/9#part2
"""

import numpy as np


class LongRope:
    def __init__(self, knot_count):
        self.knot_count = knot_count
        self.knot_positions = [(0, 0)] * self.knot_count
        self.tail_positions = {self.knot_positions[-1]}

    def _move_follower(self, mover_index):
        dif_x = self.knot_positions[mover_index - 1][0] - self.knot_positions[mover_index][0]
        dif_y = self.knot_positions[mover_index - 1][1] - self.knot_positions[mover_index][1]

        if abs(dif_x) + abs(dif_y) > 1 and not (abs(dif_x) == 1 and abs(dif_y) == 1):
            self.knot_positions[mover_index] = (
                self.knot_positions[mover_index][0] + np.sign(dif_x),
                self.knot_positions[mover_index][1] + np.sign(dif_y)
            )

        if mover_index == (self.knot_count - 1):
            self.tail_positions.update({self.knot_positions[mover_index]})

    def move_head(self, direction, distance):
        # Value pairs indicate sign of direction and axis (+1|-1, x(0)|y(1))
        direction_dictionary = {"R": (1, 0), "L": (-1, 0), "U": (1, 1), "D": (-1, 1)}
        sign, axis = direction_dictionary[direction]

        for _ in range(distance):
            if axis == 0:
                self.knot_positions[0] = (self.knot_positions[0][0] + sign, self.knot_positions[0][1])
            else:
                self.knot_positions[0] = (self.knot_positions[0][0], self.knot_positions[0][1] + sign)

            for mover_index in range(1, self.knot_count):
                self._move_follower(mover_index)
