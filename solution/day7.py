import sys

from utils.base import Day


class Day7(Day):

    def __init__(self, args):
        self.cs_fuel_levels = list(map(lambda x: int(x), args[0][0].split(',')))

    def part1(self):
        lowest_fuel_use = sys.maxsize
        for base_position in range(len(self.cs_fuel_levels)):
            total_fuel = 0

            for j in range(len(self.cs_fuel_levels)):
                total_fuel += abs(self.cs_fuel_levels[j] - base_position)

            if total_fuel <= lowest_fuel_use:
                lowest_fuel_use = total_fuel

        return lowest_fuel_use

    def part2(self):
        lowest_fuel_use = sys.maxsize
        for base_position in range(len(self.cs_fuel_levels)):
            total_fuel = 0

            for j in range(len(self.cs_fuel_levels)):
                total_fuel += sum(range(0, abs(base_position - self.cs_fuel_levels[j]) + 1))

            if total_fuel <= lowest_fuel_use:
                lowest_fuel_use = total_fuel

        return lowest_fuel_use
