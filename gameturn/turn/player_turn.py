from gameturn.game_turn import Base


class PlayerTurn(Base):
    def __init__(self):
        super().__init__()
        from gameobject.chess import ChessBoard
        self.__board = ChessBoard

    def init(self):
        self.__board.init()
        pass

    def update(self, delta_time: float()):
        super().update(delta_time)
        self.__board.update(delta_time)

    def render(self):
        self.__board.render()
