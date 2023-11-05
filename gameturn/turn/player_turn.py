from gameturn.game_turn import Base
from enum import Enum


class MousePos(Enum):
    WANT_TO_MOVE = 0,
    WANT_TO_SHOOT = 1,
    OUT_OF_BOARD = 2,
    OUT_OF_WINDOW = 3


class PlayerTurn(Base):
    def __init__(self):
        super().__init__()
        from gameobject.chess import ChessBoard
        self.__board = ChessBoard

    def init(self):
        # self.__board.init()
        pass

    def update(self, delta_time: float()):
        super().update(delta_time)
        # self.__board.update(delta_time)

    def render(self):
        # self.__board.render()
        pass
