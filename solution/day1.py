from utils.base import Day


class Day1(Day):

    def __init__(self, args):
        self.depth_levels = list(map(lambda x: int(x), args[0]))

    def part1(self):
        increases = 0
        for i in range(1, len(self.depth_levels)):
            if self.depth_levels[i-1] < self.depth_levels[i]:
                increases += 1

        return increases

    def part2(self):
        increases = 0
        for i in range(len(self.depth_levels) - 3):
            current_window = self.depth_levels[i] + self.depth_levels[i+1] + self.depth_levels[i+2]
            next_window = self.depth_levels[i+1] + self.depth_levels[i+2] + self.depth_levels[i+3]
            if current_window < next_window:
                increases += 1

        return increases
