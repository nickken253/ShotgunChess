from gameobject.chess.chess_piece import ChessPiece


class Player(ChessPiece):
    def __init__(self):
        super().__init__('B_King')
        from gameobject.chess.shotgun import Shotgun
        self.__gun = Shotgun(self)
        self.__gun.init()

    @property
    def gun(self):
        return self.__gun

    def init(self, position, health: int() = None, turn_left: int() = None, queue_size: int() = None):
        super().init(position, health, turn_left, queue_size)

    def update(self, delta_time):
        super().update(delta_time)

    def render(self):
        super().render()

    def move(self, x, y):
        super().move(x, y)
