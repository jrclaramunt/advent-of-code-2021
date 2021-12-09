from collections import defaultdict

from utils.base import Day


class Day8(Day):

    def __init__(self, args):
        self.input = list(map(lambda x: x.split('|'), args[0]))

    def part1(self):
        output_list = list(map(lambda x: x[1], self.input))
        total = 0

        for output in output_list:
            for digit in output.split():
                if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                    total += 1

        return total

    def part2(self):
        total = 0

        for line in self.input:
            digit_pattern = {}
            signal_patterns = line[0].split()
            output = line[1].split()
            sorted_by_size_signal_patters = defaultdict(list)

            signal_patterns.sort(key=lambda x: len(x))

            for i in signal_patterns:
                sorted_by_size_signal_patters[len(i)].append(i)

            digit_pattern[1] = sorted_by_size_signal_patters[2].pop()
            digit_pattern[7] = sorted_by_size_signal_patters[3].pop()
            digit_pattern[4] = sorted_by_size_signal_patters[4].pop()
            digit_pattern[8] = sorted_by_size_signal_patters[7].pop()

            for i in sorted_by_size_signal_patters[6]:
                if i.find(digit_pattern[1][0]) != -1 and i.find(digit_pattern[1][1]) != -1:
                    pass
                else:
                    digit_pattern[6] = i
                    sorted_by_size_signal_patters[6].remove(i)
                    break

            for i in sorted_by_size_signal_patters[5]:
                if len(set(digit_pattern[6]).difference(set(i))) == 1:
                    digit_pattern[5] = i
                    sorted_by_size_signal_patters[5].remove(i)
                    break

            for i in sorted_by_size_signal_patters[6]:
                if len(set(i).difference(set(digit_pattern[5]))) == 1:
                    digit_pattern[9] = i
                    sorted_by_size_signal_patters[6].remove(i)
                    break

            digit_pattern[0] = sorted_by_size_signal_patters[6].pop()

            for i in sorted_by_size_signal_patters[5]:
                if len(set(digit_pattern[9]).difference(set(i))) == 1:
                    digit_pattern[3] = i
                    sorted_by_size_signal_patters[5].remove(i)
                    break

            digit_pattern[2] = sorted_by_size_signal_patters[5].pop()

            output_number = []
            for i in output:
                for key, value in digit_pattern.items():
                    if sorted(i) == sorted(value):
                        output_number.append(str(key))

            total += int(''.join(output_number))

        return total
