from utils.base import Day


class Day4(Day):

    def __init__(self, args):
        self.drawn_numbers = list(map(lambda x: int(x), args[0][0].split(',')))
        self.bingo_board_n_lines = 5
        self.bingo_boards = []

        for i in range(2, len(args[0]), self.bingo_board_n_lines + 1):
            bingo_board = BingoBoard()
            line = 0
            for j in range(i, i + self.bingo_board_n_lines):
                bingo_board_line = list(map(lambda x: int(x), args[0][j].split()))
                bingo_board.add_line(line, bingo_board_line)
                line += 1

            self.bingo_boards.append(bingo_board)

    def part1(self):
        for number in self.drawn_numbers:
            for bingo_board in self.bingo_boards:
                bingo_board.remove_number(number)
                if bingo_board.chek_line() or bingo_board.chek_column():
                    return number * bingo_board.get_points()

    def part2(self):
        for number in self.drawn_numbers:
            for bingo_board in self.bingo_boards:
                bingo_board.remove_number(number)
                if bingo_board.chek_line() or bingo_board.chek_column():
                    bingo_board.exclude = True
                    if len(list(filter(lambda x: x.exclude is False, self.bingo_boards))) == 0:
                        return number * bingo_board.get_points()


class BingoBoard:
    def __init__(self):
        self.bingo_board_n_lines = 5
        self.board = [[] for i in range(self.bingo_board_n_lines)]
        self.exclude = False

    def add_line(self, line_number, line_content):
        self.board[line_number] = line_content

    def remove_number(self, number):
        for line in self.board:
            try:
                index = line.index(number)
                line[index] = None
            except ValueError:
                pass

    def chek_line(self):
        for line in self.board:
            if len(list(filter(lambda x: x is None, line))) == self.bingo_board_n_lines:
                return True
        return False

    def chek_column(self):
        for i in range(len(self.board)):
            marked_numbers = 0
            for j in range(len(self.board[i])):
                if self.board[j][i] is None:
                    marked_numbers += 1

                if marked_numbers == self.bingo_board_n_lines:
                    return True

        return False

    def get_points(self):
        total = 0
        for line in self.board:
            for number in list(filter(lambda x: x is not None, line)):
                total += number

        return total
