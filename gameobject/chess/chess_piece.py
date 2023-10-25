from enum import Enum

from gameobject.chess.chess_position import ChessPosition
from gameobject.sprite import Sprite


class State(Enum):
    SHOW_UP = 0
    IDLE = 1
    READY_TO_MOVE = 2
    MOVING = 3
    HURT = 4
    KILL = 5
    DEAD = 6


class Type(Enum):
    PLAYER = 0
    KING = 1
    QUEEN = 2
    BISHOP = 3
    KNIGHT = 4
    ROOK = 5
    PAWN = 6
    NOTHING = 7


class ChessPiece(Sprite):
    def __init__(self, piece_name):
        super().__init__()
        self.__name = piece_name
        self.__state = None
        self.__turn_left = None
        self.__queue_size = None
        self.__health = None
        self.__type = None
        self.__current_pos = None
        self.__dest_pos = None
        self.__shoot_pos = None
        self.__color = None
        self.is_end_turn = False
        self.__current_time = 0
        self.__is_promotion = False
        if piece_name == 'B_King':
            self.__type = Type.PLAYER
            return
        name = piece_name[2:]
        if name == "King":
            self.__type = Type.KING
        elif name == "Queen":
            self.__type = Type.QUEEN
        elif name == "Bishop":
            self.__type = Type.BISHOP
        elif name == "Knight":
            self.__type = Type.KNIGHT
        elif name == "Rook":
            self.__type = Type.ROOK
        else:
            self.__type = Type.PAWN

    @property
    def current_pos(self) -> ChessPosition:
        return self.__current_pos

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos = value
        self.position = value.position
        self.__dest_pos = value

    @property
    def dest_pos(self) -> ChessPosition:
        return self.__dest_pos

    def init(self, position, health: int() = None, turn_left: int() = None, queue_size: int() = None):
        from pygame import image
        self.texture = image.load('resource/texture/chess/piece/' + self.__name + '.png')
        self.origin = (16 / 2 * 3, 23 / 2 * 3)
        self.set_scale((3, 3))
        self.current_pos = position
        self.__state = State.SHOW_UP
        a, r, g, b = self.texture.get_colorkey()
        self.__color = 0, r, g, b
        self.is_end_turn = True
        # Only for pawn
        self.__is_promotion = False
        if self.__type == Type.PLAYER:
            return
        self.__health = 10 if health else health
        self.__queue_size = 3 if queue_size else queue_size
        from random import randint
        self.__turn_left = randint(1, self.__queue_size) if turn_left else turn_left

    def __handle_show_up(self, delta_time: float()):
        pass

    def __handle_ready(self, delta_time: float()):
        pass

    def __handle_move(self, delta_time: float()):
        pass

    def __handle_hurt(self, delta_time: float()):
        pass

    def __handle_kill(self, delta_time: float()):
        pass

    def __promote(self, name):
        pass

    def set_promotion(self, value: bool()):
        pass

    def update(self, delta_time):
        pass

    def render(self):
        from gamemanager import WConnect
        WConnect.window.blit(self.texture, self.absolute_position)
