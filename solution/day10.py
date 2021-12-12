import math

from utils.base import Day
from utils.utils import Stack


class Day10(Day):

    def __init__(self, args):
        self.navigation_subsystem = list(map(lambda x: list(x.strip()), args[0]))
        self.symbols = {
            '[': ']',
            '(': ')',
            '{': '}',
            '<': '>'
        }

        self.reverted_symbols = {v: k for k, v in self.symbols.items()}

    def part1(self):
        total = 0
        scores = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

        for line in self.navigation_subsystem:
            total += self.corrupted_score(line, scores)

        return total

    def part2(self):
        scores = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }
        total_scores = []

        for line in self.navigation_subsystem:
            stack = self.remaining_stack(line)

            if stack:
                line_total = 0
                while not stack.is_empty():
                    symbol = stack.pop()
                    line_total *= 5
                    line_total += scores[self.symbols[symbol]]

                total_scores.append(line_total)

        total_scores.sort()
        return total_scores[math.floor(len(total_scores) / 2)]

    def corrupted_score(self, line, scores):
        stack = Stack()

        for symbol in line:
            if self.is_opening_symbol(symbol):
                stack.push(symbol)
            else:
                if self.reverted_symbols[symbol] == stack.head():
                    stack.pop()
                else:
                    return scores[symbol]

        return 0

    def remaining_stack(self, line):
        stack = Stack()

        for symbol in line:
            if self.is_opening_symbol(symbol):
                stack.push(symbol)
            else:
                if self.reverted_symbols[symbol] == stack.head():
                    stack.pop()
                else:
                    return None

        return stack

    def is_opening_symbol(self, symbol):
        if symbol in self.reverted_symbols.values():
            return True

        return False
