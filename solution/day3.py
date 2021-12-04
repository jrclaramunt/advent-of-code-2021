from collections import defaultdict

from utils.base import Day


class Day3(Day):

    def __init__(self, args):
        self.diagnostic_report = list(map(lambda x: x.strip(), args[0]))
        self.n_bits = len(self.diagnostic_report[0])

    def part1(self):
        gamma_rate_sequence = []
        for i in range(self.n_bits):
            d = defaultdict(list)

            for item in self.diagnostic_report:
                d[item[i]].append(item)

            if len(d['0']) > len(d['1']):
                gamma_rate_sequence.append('0')
            else:
                gamma_rate_sequence.append('1')

        gamma_rate = int(''.join(gamma_rate_sequence), 2)
        epsilon_rate = int(''.join(list(map(lambda x: '0' if (x == '1') else '1', gamma_rate_sequence))), 2)

        return gamma_rate * epsilon_rate

    def part2(self):
        oxygen_generator_rating_list = self.diagnostic_report.copy()
        co2_scrubber_rating_list = self.diagnostic_report.copy()

        for i in range(self.n_bits):
            d = defaultdict(list)

            for diagnostic_report_item in oxygen_generator_rating_list:
                d[diagnostic_report_item[i]].append(diagnostic_report_item)

            if len(d['1']) < len(d['0']):
                oxygen_generator_rating_list = d['1']
            else:
                oxygen_generator_rating_list = d['0']

            if len(oxygen_generator_rating_list) == 1:
                break

        oxygen_generator_rating = int(''.join(oxygen_generator_rating_list[0]), 2)

        for i in range(self.n_bits):
            d = defaultdict(list)

            for diagnostic_report_item in co2_scrubber_rating_list:
                d[diagnostic_report_item[i]].append(diagnostic_report_item)

            if len(d['1']) >= len(d['0']):
                co2_scrubber_rating_list = d['1']
            else:
                co2_scrubber_rating_list = d['0']

            if len(co2_scrubber_rating_list) == 1:
                break

        co2_scrubber_rating = int(''.join(co2_scrubber_rating_list[0]), 2)

        return oxygen_generator_rating * co2_scrubber_rating
