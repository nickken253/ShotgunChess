from enum import Enum

from gameobject.chess.chess_piece import ChessPiece


class GameMode(Enum):
    EASY = 0,
    NORMAL = 1,
    HARD = 2


class GameRuleManager:
    def __init__(self):
        # Game Level
        self.current_level = 0
        self.__chess_list = []
        # Player setting
        self.shot_gun_damage = 0
        self.shot_gun_spray = 0
        self.shot_gun_range = 0
        self.shot_gun_max_ammo = 0
        self.shot_gun_max_capacity = 0
        # Chess setting
        self.price_list = dict()
        self.health_list = dict()
        self.queue_size_list = dict()
        self.set_mode(GameMode.EASY)

    def set_mode(self, value):
        self.current_level = 0
        from gameobject.chess.chess_piece import Type
        if value == GameMode.EASY:
            # Player gun
            self.shot_gun_damage = 5
            self.shot_gun_range = 350
            self.shot_gun_spray = 7
            self.shot_gun_max_ammo = 2
            self.shot_gun_max_capacity = 8
            # Chess price
            self.price_list[Type.KING] = 800
            self.price_list[Type.QUEEN] = 600
            self.price_list[Type.BISHOP] = 350
            self.price_list[Type.KNIGHT] = 350
            self.price_list[Type.ROOK] = 400
            self.price_list[Type.PAWN] = 250
            # Chess health
            self.health_list[Type.KING] = 8
            self.health_list[Type.QUEEN] = 6
            self.health_list[Type.BISHOP] = 4
            self.health_list[Type.KNIGHT] = 3
            self.health_list[Type.ROOK] = 5
            self.health_list[Type.PAWN] = 3
            # Chess queue size
            self.queue_size_list[Type.KING] = 4
            self.queue_size_list[Type.QUEEN] = 3
            self.queue_size_list[Type.BISHOP] = 3
            self.queue_size_list[Type.KNIGHT] = 2
            self.queue_size_list[Type.ROOK] = 4
            self.queue_size_list[Type.PAWN] = 5
        elif value == GameMode.NORMAL:
            pass
        elif value == GameMode.HARD:
            pass

    def level1(self):
        from gameobject.chess.player import Player
        from gameobject.chess.chess_piece import ChessPiece, Type
        from gameobject.chess.chess_position import ChessPosition
        player = Player()
        player.init(ChessPosition(3, 7))
        self.__chess_list.append(player)

        king = ChessPiece('W_King')
        king.init(ChessPosition(3, 0))
        king.health = self.health_list[Type.QUEEN]
        self.__chess_list.append(king)

        for i in range(2, 6):
            pawn = ChessPiece('W_Pawn')
            pawn.init(ChessPosition(i, 1))
            self.__chess_list.append(pawn)

        knight = ChessPiece('W_Knight')
        knight.init(ChessPosition(4, 0))
        self.__chess_list.append(knight)
        pass

    def level2(self):
        pass

    def level3(self):
        pass

    def level4(self):
        pass

    def level5(self):
        pass

    def level_init(self, n: int()):
        self.__chess_list.clear()
        if n == 1:
            self.level1()
        elif n == 2:
            self.level2()
        elif n == 3:
            self.level3()
        elif n == 4:
            self.level4()
        elif n == 5:
            self.level5()
        self.current_level = n

    def get_chess_list(self, level: int()) -> list[ChessPiece]:
        self.level_init(level)
        return sorted(self.__chess_list, key=lambda x: x.current_pos)
