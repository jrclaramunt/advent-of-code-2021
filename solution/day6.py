from utils.base import Day


class Day6(Day):

    def __init__(self, args):
        self.input = list(map(lambda x: int(x), args[0][0].split(',')))

    def breeding_process(self, days):
        breeding_times_count = {}
        newborn_breeding_time = 8
        reset_breeding_time = 6

        for i in range(newborn_breeding_time + 1):
            breeding_times_count[i] = 0

        for i in self.input:
            breeding_times_count[i] += 1

        for day in range(days):
            resets = 0
            newborns = 0

            if breeding_times_count[0] != 0:
                resets = breeding_times_count[0]
                newborns = breeding_times_count[0]
                breeding_times_count[0] = 0

            for key in breeding_times_count.keys():
                if key != 0:
                    breeding_times_count[key - 1] = breeding_times_count[key]

            breeding_times_count[reset_breeding_time] += resets
            breeding_times_count[newborn_breeding_time] = newborns

        return sum(breeding_times_count.values())

    def part1(self):
        return self.breeding_process(80)

    def part2(self):
        return self.breeding_process(256)
