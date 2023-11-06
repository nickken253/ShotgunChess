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
            # Player gun
            self.shot_gun_damage = 4
            self.shot_gun_range = 300
            self.shot_gun_spray = 6
            self.shot_gun_max_ammo = 2
            self.shot_gun_max_capacity = 6
            # Chess price
            self.price_list[Type.KING] = 1000
            self.price_list[Type.QUEEN] = 800
            self.price_list[Type.BISHOP] = 400
            self.price_list[Type.KNIGHT] = 4000
            self.price_list[Type.ROOK] = 500
            self.price_list[Type.PAWN] = 300
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
        elif value == GameMode.HARD:
            # Player gun
            self.shot_gun_damage = 3
            self.shot_gun_range = 250
            self.shot_gun_spray = 6
            self.shot_gun_max_ammo = 1
            self.shot_gun_max_capacity = 5
            # Chess price
            self.price_list[Type.KING] = 1000
            self.price_list[Type.QUEEN] = 800
            self.price_list[Type.BISHOP] = 400
            self.price_list[Type.KNIGHT] = 400
            self.price_list[Type.ROOK] = 500
            self.price_list[Type.PAWN] = 300
            # Chess health
            self.health_list[Type.KING] = 9
            self.health_list[Type.QUEEN] = 7
            self.health_list[Type.BISHOP] = 5
            self.health_list[Type.KNIGHT] = 4
            self.health_list[Type.ROOK] = 6
            self.health_list[Type.PAWN] = 4
            # Chess queue size
            self.queue_size_list[Type.KING] = 4
            self.queue_size_list[Type.QUEEN] = 3
            self.queue_size_list[Type.BISHOP] = 3
            self.queue_size_list[Type.KNIGHT] = 2
            self.queue_size_list[Type.ROOK] = 4
            self.queue_size_list[Type.PAWN] = 5

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

    def level2(self):
        from gameobject.chess.player import Player
        from gameobject.chess.chess_piece import ChessPiece, Type
        from gameobject.chess.chess_position import ChessPosition
        player = Player()
        player.init(ChessPosition(4, 7))
        self.__chess_list.append(player)

        king = ChessPiece('W_King')
        king.init(ChessPosition(3, 0))
        king.health = self.health_list[Type.QUEEN]
        self.__chess_list.append(king)

        for i in range(2, 6):
            pawn = ChessPiece('W_Pawn')
            pawn.init(ChessPosition(i, 1))
            self.__chess_list.append(pawn)

        bishop = ChessPiece('W_Bishop')
        bishop.init(ChessPosition(2, 0))
        self.__chess_list.append(bishop)

        rook = ChessPiece('W_Rook')
        rook.init(ChessPosition(4, 0))
        self.__chess_list.append(rook)

        knight = ChessPiece('W_Knight')
        knight.init(ChessPosition(5, 0))
        self.__chess_list.append(knight)

    def level3(self):
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

        for i in range(1, 7):
            pawn = ChessPiece('W_Pawn')
            pawn.init(ChessPosition(i, 1))
            self.__chess_list.append(pawn)

        for i in [0, 7]:
            rook = ChessPiece('W_Rook')
            rook.init(ChessPosition(i, 0))
            self.__chess_list.append(rook)

        for i in [2, 5]:
            bishop = ChessPiece('W_Bishop')
            bishop.init(ChessPosition(i, 0))
            self.__chess_list.append(bishop)

        knight = ChessPiece('W_Knight')
        knight.init(ChessPosition(4, 0))
        self.__chess_list.append(knight)

    def level4(self):
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

        for i in [0, 6, 7]:
            knight = ChessPiece('W_Knight')
            knight.init(ChessPosition(i, 0))
            self.__chess_list.append(knight)

        for i in [1, 5]:
            bishop = ChessPiece('W_Bishop')
            bishop.init(ChessPosition(i, 0))
            self.__chess_list.append(bishop)

        for i in [2, 4]:
            rook = ChessPiece('W_Rook')
            rook.init(ChessPosition(i, 0))
            self.__chess_list.append(rook)


    def level5(self):
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

        queen = ChessPiece('W_Queen')
        queen.init(ChessPosition(4, 0))
        self.__chess_list.append(queen)

        for i in range(0, 8):
            pawn = ChessPiece('W_Pawn')
            pawn.init(ChessPosition(i, 1))
            self.__chess_list.append(pawn)

        for i in [0, 7]:
            rook = ChessPiece('W_Rook')
            rook.init(ChessPosition(i, 0))
            self.__chess_list.append(rook)

        for i in [1, 6]:
            knight = ChessPiece('W_Knight')
            knight.init(ChessPosition(i, 0))
            self.__chess_list.append(knight)

        for i in [2, 5]:
            bishop = ChessPiece('W_Bishop')
            bishop.init(ChessPosition(i, 0))
            self.__chess_list.append(bishop)

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
        return self.__chess_list
