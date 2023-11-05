from gamemanager.singleton import Singleton
from gameobject.chess.chess_position import ChessPosition
from gameobject.chess.chess_piece import ChessPiece


class ChessMoveGenerator(metaclass=Singleton):
    def __init__(self):
        self.__player_position = None
        self.__has_piece = [[False for _ in range(8)] for _ in range(8)]

    def get_next_move(self, piece: ChessPiece):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type
        self.__player_position = ChessBoard.player.current_pos
        move_list = []
        if piece.type == Type.PAWN:
            return self.get_pawn_move(piece.current_pos)
        elif piece.type == Type.KING:
            move_list = self.get_king_move(piece.current_pos)
        elif piece.type == Type.QUEEN:
            move_list = self.get_queen_move(piece.current_pos)
        elif piece.type == Type.BISHOP:
            move_list = self.get_bishop_move(piece.current_pos)
        elif piece.type == Type.KNIGHT:
            move_list = self.get_knight_move(piece.current_pos)
        elif piece.type == Type.ROOK:
            move_list = self.get_rook_move(piece.current_pos)
        next_pos = piece.current_pos
        for pos in move_list:
            if pos == self.__player_position:
                return pos
            if self.__valid_move(pos) is False:
                continue
            if next_pos == piece.current_pos:
                next_pos = pos
                continue
            if self.__position_compare(pos, next_pos):
                next_pos = pos
        return next_pos

    def __position_compare(self, a: ChessPosition, b: ChessPosition) -> bool:
        from utils import GMath
        d_a = GMath.get_distance(a.position, self.__player_position.position)
        d_b = GMath.get_distance(b.position, self.__player_position.position)
        return d_a <= d_b

    def __valid_move(self, pos: ChessPosition) -> bool:
        if pos.x < 0 or pos.y < 0 or pos.x > 7 or pos.y > 7:
            return False
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                if pos == piece.current_pos or pos == piece.dest_pos:
                    return False
        return True

    def get_king_move(self, pos: ChessPosition) -> list[ChessPosition]:
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        move_list = []
        for i in range(8):
            tmp_pos = ChessPosition(pos.x + dx[i], pos.y + dy[i])
            if self.__valid_move(tmp_pos) is False:
                continue
            move_list.append(tmp_pos)
        return move_list

    def get_queen_move(self, pos: ChessPosition) -> list[ChessPosition]:
        move_list = self.get_rook_move(pos).copy()
        bishop_move = self.get_bishop_move(pos)
        for move in bishop_move:
            move_list.append(move)
        return move_list

    def get_bishop_move(self, pos: ChessPosition) -> list[ChessPosition]:
        move_list = []
        i = 1
        while pos.x + i <= 7 and pos.y + i <= 7:
            tmp_pos = ChessPosition(pos.x + i, pos.y + i)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        i = 1
        while pos.x - i >= 0 and pos.y - i >= 0:
            tmp_pos = ChessPosition(pos.x - i, pos.y - i)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        i = 1
        while pos.x + i <= 7 and pos.y - i >= 0:
            tmp_pos = ChessPosition(pos.x + i, pos.y - i)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        i = 1
        while pos.x - i >= 0 and pos.y + i <= 7:
            tmp_pos = ChessPosition(pos.x - i, pos.y + i)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        return move_list

    def get_rook_move(self, pos: ChessPosition) -> list[ChessPosition]:
        move_list = []
        i = 1
        while pos.x + i <= 7:
            tmp_pos = ChessPosition(pos.x + i, pos.y)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        i = 1
        while pos.x - i >= 0:
            tmp_pos = ChessPosition(pos.x - i, pos.y)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        i = 1
        while pos.y + i <= 7:
            tmp_pos = ChessPosition(pos.x, pos.y + i)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1

        i = 1
        while pos.y - i >= 0:
            tmp_pos = ChessPosition(pos.x, pos.y - i)
            if self.__valid_move(tmp_pos) is False:  # the path is blocked
                break
            move_list.append(tmp_pos)
            i += 1
        return move_list

    def get_knight_move(self, pos: ChessPosition) -> list[ChessPosition]:
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        move_list = []
        for i in range(8):
            tmp_pos = ChessPosition(pos.x + dx[i], pos.y + dy[i])
            if self.__valid_move(tmp_pos) is False:
                continue
            move_list.append(tmp_pos)
        return move_list

    def get_pawn_move(self, pos: ChessPosition) -> ChessPosition:
        if pos.y == 7:
            return pos
        next_pos = ChessPosition(pos.x, pos.y + 1)
        if next_pos == self.__player_position:
            if next_pos.x == self.__player_position.x:
                return pos
            elif next_pos.x - 1 == self.__player_position.x:
                next_pos.x -= 1
            elif next_pos.x + 1 == self.__player_position.x:
                next_pos.x += 1
        if self.__valid_move(next_pos):
            return next_pos
        else:
            return pos
