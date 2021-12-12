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
