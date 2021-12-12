from utils.base import Day
from utils.utils import Coordinate


class Day11(Day):

    def __init__(self, args):
        self.input = args[0]

    def part1(self):
        total_flashes = 0

        self.reset()

        for i in range(100):
            self.step()

            while len(self.to_flash) > 0:
                flashing = self.to_flash.pop()
                total_flashes += 1
                self.energy_levels[flashing.x][flashing.y] = 0
                self.increase_up(flashing.x, flashing.y)
                self.increase_up_right(flashing.x, flashing.y)
                self.increase_right(flashing.x, flashing.y)
                self.increase_down_right(flashing.x, flashing.y)
                self.increase_down(flashing.x, flashing.y)
                self.increase_down_left(flashing.x, flashing.y)
                self.increase_left(flashing.x, flashing.y)
                self.increase_up_left(flashing.x, flashing.y)

        return total_flashes

    def part2(self):
        current_step = 0

        self.reset()

        while 1:
            self.step()
            current_step += 1

            while len(self.to_flash) > 0:
                flashing = self.to_flash.pop()
                self.energy_levels[flashing.x][flashing.y] = 0
                self.increase_up(flashing.x, flashing.y)
                self.increase_up_right(flashing.x, flashing.y)
                self.increase_right(flashing.x, flashing.y)
                self.increase_down_right(flashing.x, flashing.y)
                self.increase_down(flashing.x, flashing.y)
                self.increase_down_left(flashing.x, flashing.y)
                self.increase_left(flashing.x, flashing.y)
                self.increase_up_left(flashing.x, flashing.y)

            length = 0
            flashed = 0
            for i in range(len(self.energy_levels)):
                flashed += self.energy_levels[i].count(0)
                length += len(self.energy_levels[i])

            if flashed == length:
                return current_step

    def step(self):
        for i in range(len(self.energy_levels)):
            for j in range(len(self.energy_levels[i])):
                self.energy_levels[i][j] += 1
                if self.energy_levels[i][j] > 9:
                    self.to_flash.add(Coordinate(i, j))

    def increase_up(self, i, j):
        if self.in_check_range(i - 1, j):
            if self.energy_levels[i - 1][j] != 0:
                self.energy_levels[i - 1][j] += 1
            if self.energy_levels[i - 1][j] > 9:
                self.to_flash.add(Coordinate(i - 1, j))

    def increase_up_right(self, i, j):
        if self.in_check_range(i - 1, j + 1):
            if self.energy_levels[i - 1][j + 1] != 0:
                self.energy_levels[i - 1][j + 1] += 1
            if self.energy_levels[i - 1][j + 1] > 9:
                self.to_flash.add(Coordinate(i - 1, j + 1))

    def increase_right(self, i, j):
        if self.in_check_range(i, j + 1):
            if self.energy_levels[i][j + 1] != 0:
                self.energy_levels[i][j + 1] += 1
            if self.energy_levels[i][j + 1] > 9:
                self.to_flash.add(Coordinate(i, j + 1))

    def increase_down_right(self, i, j):
        if self.in_check_range(i + 1, j + 1):
            if self.energy_levels[i + 1][j + 1] != 0:
                self.energy_levels[i + 1][j + 1] += 1
            if self.energy_levels[i + 1][j + 1] > 9:
                self.to_flash.add(Coordinate(i + 1, j + 1))

    def increase_down(self, i, j):
        if self.in_check_range(i + 1, j):
            if self.energy_levels[i + 1][j] != 0:
                self.energy_levels[i + 1][j] += 1
            if self.energy_levels[i + 1][j] > 9:
                self.to_flash.add(Coordinate(i + 1, j))

    def increase_down_left(self, i, j):
        if self.in_check_range(i + 1, j - 1):
            if self.energy_levels[i + 1][j - 1] != 0:
                self.energy_levels[i + 1][j - 1] += 1
            if self.energy_levels[i + 1][j - 1] > 9:
                self.to_flash.add(Coordinate(i + 1, j - 1))

    def increase_left(self, i, j):
        if self.in_check_range(i, j - 1):
            if self.energy_levels[i][j - 1] != 0:
                self.energy_levels[i][j - 1] += 1
            if self.energy_levels[i][j - 1] > 9:
                self.to_flash.add(Coordinate(i, j - 1))

    def increase_up_left(self, i, j):
        if self.in_check_range(i - 1, j - 1):
            if self.energy_levels[i - 1][j - 1] != 0:
                self.energy_levels[i - 1][j - 1] += 1
            if self.energy_levels[i - 1][j - 1] > 9:
                self.to_flash.add(Coordinate(i - 1, j - 1))

    def in_check_range(self, i, j):
        return 0 <= i < len(self.energy_levels) and 0 <= j < len(self.energy_levels[i])

    def reset(self):
        self.to_flash = set()
        self.energy_levels = []

        for line in self.input:
            self.energy_levels.append(list(map(int, line.strip())))
