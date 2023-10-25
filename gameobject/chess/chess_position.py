class ChessPosition:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def position(self):
        board_x, board_y = 382.0, 120.0
        offset_x = self.x * 64.5 + 64.5 / 2
        offset_y = self.y * 64.5 + 23.0 / 2 + 5.0
        return board_x + offset_x, board_y + offset_y

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y < other.y

    def __gt__(self, other):
        if self.y == other.y:
            return self.x > other.x
        else:
            return self.y > other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
