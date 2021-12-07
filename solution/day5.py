import re

from utils.base import Day
from utils.utils import Coordinate


class Day5(Day):
    def __init__(self, args):
        self.size_x = 0
        self.size_y = 0
        self.lines = []
        regex = r'(\d+),(\d+) -> (\d+),(\d+)'
        for line in args[0]:
            coordinates = list(map(lambda x: int(x), re.match(regex, line.strip()).groups()))
            line = Line(coordinates)
            self.size_x = max(line.a.x, line.b.x, self.size_x)
            self.size_y = max(line.a.y, line.b.y, self.size_y)
            self.lines.append(Line(coordinates))

    def part1(self):
        lines_map = [[0] * (self.size_y + 1) for i in range(self.size_x + 1)]

        for line in self.lines:
            if not line.is_diagonal():
                for coordinate in line.coordinates():
                    lines_map[coordinate.y][coordinate.x] += 1

        total = 0
        for row in lines_map:
            total += len(list(filter(lambda x: x >= 2, row)))

        return total

    def part2(self):
        lines_map = [[0] * (self.size_y + 1) for i in range(self.size_x + 1)]
        for line in self.lines:
            for coordinate in line.coordinates():
                lines_map[coordinate.y][coordinate.x] += 1

        total = 0
        for row in lines_map:
            total += len(list(filter(lambda x: x >= 2, row)))

        return total


class Line:
    def __init__(self, coordinates):
        self.a = Coordinate(coordinates[0], coordinates[1])
        self.b = Coordinate(coordinates[2], coordinates[3])

    def __str__(self):
        return f'({self.a.x},{self.a.y}) -> ({self.b.x},{self.b.y})'

    def is_horizontal(self):
        return self.a.y == self.b.y

    def is_vertical(self):
        return self.a.x == self.b.x

    def is_diagonal(self):
        return abs(self.a.x - self.b.x) == abs(self.a.y - self.b.y)

    def coordinates(self):
        coordinates = []
        if self.is_vertical():
            step = 1 if (self.a.y < self.b.y) else -1

            for i in range(self.a.y, self.b.y + step, step):
                coordinates.append(Coordinate(self.a.x, i))

            return coordinates

        if self.is_horizontal():
            step = 1 if (self.a.x < self.b.x) else -1

            for i in range(self.a.x, self.b.x + step, step):
                coordinates.append(Coordinate(i, self.a.y))

            return coordinates

        if self.is_diagonal():
            step_x = 1 if (self.a.x < self.b.x) else -1
            step_y = 1 if (self.a.y < self.b.y) else -1

            y = self.a.y
            for i in range(self.a.x, self.b.x + step_x, step_x):
                coordinates.append(Coordinate(i, y))
                y += step_y

            return coordinates
