class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __members(self):
        return self.x, self.y

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__members() == other.__members()
        else:
            return False

    def __hash__(self):
        return hash(self.__members())


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop(len(self.stack) - 1)

    def head(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return len(self.stack) == 0
