from enum import Enum

from utils.base import Day


class Day2(Day):

    def __init__(self, args):
        self.instructions = list(args[0])

    def part1(self):
        x = 0
        depth = 0

        for line in self.instructions:
            command = Command(line)

            if command.instruction == Instructions.FORWARD.value:
                x += command.units
            elif command.instruction == Instructions.DOWN.value:
                depth += command.units
            elif command.instruction == Instructions.UP.value:
                depth -= command.units
            else:
                raise InvalidInstructionException()

        return x * depth

    def part2(self):
        x = 0
        depth = 0
        aim = 0

        for line in self.instructions:
            command = Command(line)

            if command.instruction == Instructions.FORWARD.value:
                x += command.units
                depth += aim * command.units
            elif command.instruction == Instructions.DOWN.value:
                aim += command.units
            elif command.instruction == Instructions.UP.value:
                aim -= command.units
            else:
                raise InvalidInstructionException()

        return x * depth


class Command:

    def __init__(self, line):
        self.instruction = line.split()[0]
        self.units = int(line.split()[1])


class Instructions(Enum):
    FORWARD = 'forward'
    UP = 'up'
    DOWN = 'down'


class InvalidInstructionException(Exception):
    pass
