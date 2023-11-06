from enum import Enum

from gamemanager.singleton import Singleton


class Turn(Enum):
    SHOW_UP = 0
    PLAYER = 1
    BOT = 2
    WIN = 3
    LOSE = 4


class Base:
    def __init__(self):
        self.isPerforming = False

    def init(self):
        pass

    def update(self, delta_time: float()):
        pass

    def render(self):
        pass

    @classmethod
    def create_turn(cls, turn: Turn):
        if turn == Turn.SHOW_UP:
            from gameturn.turn.show_up_turn import ShowupTurn
            return ShowupTurn()
        if turn == Turn.PLAYER:
            from gameturn.turn.player_turn import PlayerTurn
            return PlayerTurn()
        if turn == Turn.BOT:
            from gameturn.turn.bot_turn import BotTurn
            return BotTurn()
        if turn == Turn.WIN:
            from gameturn.turn.win_turn import WinTurn
            return WinTurn()
        if turn == Turn.LOSE:
            from gameturn.turn.lose_turn import LoseTurn
            return LoseTurn()
        return Base()


class Machine(metaclass=Singleton):
    def __init__(self):
        self.__turn_count = -1  # Showing up turn will start at 0
        self.__current_turn = None
        self.__next_turn = None

    @property
    def current_turn(self) -> Base:
        return self.__current_turn

    @property
    def next_turn(self) -> Base:
        return self.__next_turn

    @property
    def turn_count(self):
        return self.turn_count

    @property
    def need_to_change_turn(self):
        return self.__next_turn is not None

    def reset_count(self):
        self.__turn_count = -1

    def change_turn(self, turn: Turn):
        game_turn = Base.create_turn(turn)
        self.__next_turn = game_turn

    def perform_change(self):
        self.__turn_count += 1
        if self.__next_turn is not None:
            self.__current_turn = self.__next_turn
            self.__current_turn.init()
            self.__next_turn = None
