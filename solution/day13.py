import re

from utils.base import Day
from utils.utils import Coordinate


class Day13(Day):
    def __init__(self, args):
        self.coordinates = []
        self.folding_instructions = []

        index = 0
        self.length_x = 0
        self.length_y = 0

        for line in args[0]:
            if line == '\n':
                break
            coordinate = line.strip().split(',')
            x = int(coordinate[0])
            y = int(coordinate[1])
            self.coordinates.append(Coordinate(x, y))

            self.length_x = max(self.length_x, x)
            self.length_y = max(self.length_y, y)

            index += 1

        regex = r'fold along (x|y)=(\d+)'
        for i in range(index + 1, len(args[0])):
            folding = re.match(regex, args[0][i]).groups()
            self.folding_instructions.append((folding[0], int(folding[1])))

        self.transparent_paper = [['.'] * (self.length_x + 1) for i in range(self.length_y + 1)]
        for coordinate in self.coordinates:
            self.transparent_paper[coordinate.y][coordinate.x] = '#'

    def part1(self):
        fold = FoldManager(self.transparent_paper.copy())
        dot_map = fold.fold(self.folding_instructions[:1])

        total = 0
        for i in dot_map:
            total += i.count('#')

        return total

    def part2(self):
        fold = FoldManager(self.transparent_paper.copy())
        transparent_paper = fold.fold(self.folding_instructions)

        for line in transparent_paper:
            line.reverse()
            print(''.join(line))


class FoldManager:
    def __init__(self, transparent_paper):
        self.transparent_paper = transparent_paper

    def fold(self, folding_instructions):
        for instruction in folding_instructions:
            if instruction[0] == 'y':
                self.fold_y(instruction[1])
            else:
                self.fold_x(instruction[1])

        return self.transparent_paper

    def fold_x(self, position):
        for i in range(len(self.transparent_paper)):
            for j in range(position):
                if self.transparent_paper[i][j] == '#':
                    self.transparent_paper[i][position + (position - j)] = '#'

        self.transparent_paper = [sublist[position + 1:] for sublist in self.transparent_paper]

    def fold_y(self, position):
        for i in range(position + 1, len(self.transparent_paper)):
            for j in range(len(self.transparent_paper[i])):
                if self.transparent_paper[i][j] == '#':
                    self.transparent_paper[position - (i - position)][j] = '#'

        self.transparent_paper = self.transparent_paper[:position]
