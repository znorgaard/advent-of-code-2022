# -*- coding: utf-8 -*-

"""
Puzzle prompts are getting long, go see it here:
https://adventofcode.com/2022/day/10
https://adventofcode.com/2022/day/10#part2
"""

import logging
logging.basicConfig(level=logging.DEBUG)


class Communicator:
    def __init__(self):
        """ Communicator initialization """
        self.x = 1
        self.cycle = 0
        self.interesting_cycles = []
        self.image = []

    def run_cycle(self, x=0):
        """ Run a cycle and update X as needed
          - Increments the cycle
          - Updates the image string
          - Record interesting signal strength
          - Move sprite (aka update X)

        Args:
            x the integer amount to adjust x by
        """
        # Start cycle
        self.cycle += 1
        # Update image
        if self.x - 1 <= (self.cycle - 1) % 40 <= self.x + 1:
            self.image.append("#")
        else:
            self.image.append(".")
        # Record interesting signal
        if self.cycle % 40 == 20:
            self.interesting_cycles.append((self.cycle, self.cycle * self.x))
        # Move sprite
        self.x += x

    def follow_instructions(self, instruction):
        """ Parse provided instructions

        Args:
            instruction: One of "noop", no operation, or "addx #", update X
        """
        if instruction == "noop":
            self.run_cycle()
        else:
            self.run_cycle()
            self.run_cycle(int(instruction.split(" ")[1]))

    def sum_interesting_cycles(self, max_cycle=220):
        """ Calculate sum of signal strength at interesting cycles (20 and every 40th cycle after that up to a limit)

        Args:
            max_cycle: the maximum cycle to consider interesting
        Returns:
            sum of signal strength at interesting cycles (20 and every 40th cycle after that up to a limit)
        """
        return sum([signal for cycle, signal in self.interesting_cycles if cycle <= max_cycle])

    def get_image(self):
        """ Get image displayed on screen

        Returns:
            string representing the screen display
        """
        return "\n".join(["".join(self.image[i * 40: i * 40 + 40]) for i in range(6)])
