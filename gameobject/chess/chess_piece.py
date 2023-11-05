import math
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
        self.turn_left = None
        self.queue_size = None
        self.health = None
        self.type = None
        self.__current_pos = None
        self.__dest_pos = None
        self.__shoot_pos = None
        # self.__color = None
        self.is_end_turn = False
        self.__current_time = 0
        self.__is_promotion = False
        if piece_name == 'B_King':
            self.type = Type.PLAYER
            return
        name = piece_name[2:]
        if name == "King":
            self.type = Type.KING
        elif name == "Queen":
            self.type = Type.QUEEN
        elif name == "Bishop":
            self.type = Type.BISHOP
        elif name == "Knight":
            self.type = Type.KNIGHT
        elif name == "Rook":
            self.type = Type.ROOK
        else:
            self.type = Type.PAWN

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

    @dest_pos.setter
    def dest_pos(self, value):
        self.__dest_pos = value

    @property
    def shoot_pos(self) -> ChessPosition:
        return self.__shoot_pos

    @shoot_pos.setter
    def shoot_pos(self, value):
        self.__shoot_pos = value

    def perform_turn(self):
        self.__current_time = 0
        self.is_end_turn = False

    @property
    def state(self) -> State:
        return self.__state

    @state.setter
    def state(self, value):
        self.__current_time = 0
        self.__state = value

    def count_turn_left(self):
        if self.type == Type.PLAYER:
            return
        self.turn_left -= 1
        if self.turn_left < 0:
            self.turn_left = self.queue_size
        if self.turn_left == 1:
            self.state = State.READY_TO_MOVE
        else:
            self.state = State.IDLE

    def init(self, position, health: int() = None, turn_left: int() = None, queue_size: int() = None):
        from gamemanager import DATA
        self.texture = DATA.get_texture("\\chess\\piece\\" + self.__name)
        self.origin = (8, 23 / 2)
        self.scale = (3, 3)
        self.current_pos = position
        self.__state = State.SHOW_UP
        self.alpha = 0
        self.is_end_turn = True
        # Only for pawn
        self.__is_promotion = False
        if self.type == Type.PLAYER:
            return
        from gameobject import GRM
        self.health = GRM.health_list[self.type]
        self.queue_size = GRM.queue_size_list[self.type]
        from random import randint
        self.turn_left = randint(1, self.queue_size)

    def __handle_show_up(self, delta_time: float()):
        from utils import GMath
        import game_config
        self.__current_time += delta_time
        if self.__current_time < game_config.SHOW_UP_DURATION:
            offset_y = GMath.get_harmonic_motion(game_config.SHOW_UP_OFFSET, game_config.SHOW_UP_DURATION,
                                                 self.__current_time)
            pos = self.current_pos.position
            pos = (pos[0], pos[1] + offset_y)
            self.position = pos
        else:
            self.current_pos = self.__current_pos
            # DATA->playSound("drop1");

        if self.__current_time < game_config.SHOW_UP_DURATION / 2:
            color_a = min(255, int(round(255 * self.__current_time / (game_config.SHOW_UP_DURATION / 2))))
            self.alpha = color_a
        elif self.__current_time > game_config.SHOW_UP_DURATION:
            color_a = 255
            self.alpha = color_a
            self.state = State.IDLE
            self.is_end_turn = True
        pass

    def __handle_ready(self, delta_time: float()):
        self.__current_time += delta_time
        from utils import GMath
        import game_config
        x = 8.0 + GMath.get_harmonic_motion(game_config.BUZZING_OFFSET, game_config.BUZZING_DURATION,
                                            self.__current_time)
        self.origin = (x, self.origin[1])
        pass

    def __handle_move(self, delta_time: float()):
        self.__current_time += delta_time
        from utils import GMath
        import game_config
        if self.__current_time < game_config.MOVING_DURATION:
            pos = GMath.get_moving_equation(self.current_pos.position, self.dest_pos.position,
                                            game_config.MOVING_DURATION, self.__current_time)
            offset_y = GMath.get_harmonic_motion(40.0, game_config.MOVING_DURATION, self.__current_time)
            pos = (pos[0], pos[1] + offset_y)
            self.position = pos
        else:
            self.current_pos = self.dest_pos
            self.state = State.IDLE
            if self.type != Type.PLAYER:
                self.count_turn_left()
                # DATA->playSound("drop2");
            else:
                # DATA->playSound("drop3");
                pass
            self.is_end_turn = True
        pass

    def __handle_hurt(self, delta_time: float()):
        from utils import GMath
        import game_config
        self.__current_time += delta_time
        if self.__current_time < game_config.HURT_DURATION:
            angle = GMath.get_angle(self.current_pos.position, self.__shoot_pos.position)
            k = GMath.get_harmonic_motion(game_config.HURT_OFFSET, game_config.HURT_DURATION, self.__current_time)
            if k < -game_config.HURT_DURATION / 2:
                self.colorkey = game_config.HURT_COLOR
            else:
                self.colorkey = None
            x = 8.0 - k * math.cos(angle)
            y = 23 / 2 - k * math.sin(angle)
            self.origin = (x, y)
        else:
            self.origin = (8, 23 / 2)
            self.state = State.IDLE
            self.is_end_turn = True
        pass

    def __handle_kill(self, delta_time: float()):
        self.__current_time += delta_time
        from utils import GMath
        import game_config
        if self.__current_time < game_config.HURT_DURATION / 2:
            angle = GMath.get_angle(self.current_pos.position, self.__shoot_pos.position)
            k = GMath.get_harmonic_motion(game_config.HURT_OFFSET, game_config.HURT_DURATION, self.__current_time)
            x = 8 - k * math.cos(angle)
            y = 23 / 2 - k * math.sin(angle)
            self.origin = (x, y)
            if k < -game_config.HURT_OFFSET / 2:
                self.colorkey = game_config.HURT_COLOR
        elif self.__current_time < game_config.KILL_DURATION:
            color = game_config.HURT_COLOR
            color_a = int(
                max(0, (1 - self.__current_time / (game_config.KILL_DURATION - game_config.HURT_DURATION / 2)) * 255))
            self.alpha = color_a
        else:
            self.state = State.DEAD
            self.is_end_turn = True
        pass

    def __promote(self, name):
        if self.type != Type.PAWN or self.__is_promotion is False:
            return
        # re-construct
        self.__name = "\\chess\\piece\\" + name
        # set chess piece type
        name = name[2:]
        if name == "King":
            self.type = Type.KING
        elif name == "Queen":
            self.type = Type.QUEEN
        elif name == "Bishop":
            self.type = Type.BISHOP
        elif name == "Knight":
            self.type = Type.KNIGHT
        elif name == "Rook":
            self.type = Type.ROOK
        else:
            self.type = Type.PAWN
        # re-init
        from gamemanager import DATA
        self.texture = DATA.get_texture(name)
        # self.__color = self.texture.get_colorkey()
        from gameobject import GRM
        self.health = GRM.health_list[self.type]
        self.queue_size = GRM.queue_size_list[self.type]
        self.turn_left = self.queue_size - 1
        self.__is_promotion = False
        pass

    def set_promotion(self, value: bool()):
        self.__is_promotion = value
        pass

    def update(self, delta_time):
        if self.state == State.SHOW_UP:
            self.__handle_show_up(delta_time)
        elif self.state == State.IDLE:
            if self.__is_promotion:
                from random import choice
                promote_list = ["W_Queen", "W_Knight", "W_Rook", "W_Bishop"]
                self.__promote(choice(promote_list))
        elif self.state == State.READY_TO_MOVE:
            self.__handle_ready(delta_time)
        elif self.state == State.MOVING:
            self.__handle_move(delta_time)
        elif self.state == State.HURT:
            self.__handle_hurt(delta_time)
        elif self.state == State.KILL:
            self.__handle_kill(delta_time)
        elif self.state == State.DEAD:
            pass

    def render(self):
        from gamemanager import WConnect
        WConnect.window.blit(self.texture, self.absolute_position)

    def take_damage(self, dmg):
        if self.__state == State.HURT:
            return
        self.health -= dmg
