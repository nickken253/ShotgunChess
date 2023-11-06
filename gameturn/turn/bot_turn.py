from gameturn.game_turn import Base


class BotTurn(Base):
    def __init__(self):
        super().__init__()
        self.__player_position = None
        self.__is_player_killable = False

    def init(self):
        from gameobject.chess import ChessBoard
        for piece in ChessBoard.chess_list:
            piece.is_end_turn = True
        ChessBoard.player.gun.set_shootable(False)
        self.isPerforming = False
        self.__is_player_killable = False
        self.__player_position = ChessBoard.player.current_pos

    def update(self, delta_time: float):
        from gameturn import GTM
        from gameturn.game_turn import Turn
        from gameobject.chess import ChessBoard
        if self.__is_player_killable:
            GTM.change_turn(Turn.LOSE)

        if self.isPerforming is False:
            self.__handle_bot_event()
        else:
            if self.__is_end_bot_turn():
                GTM.change_turn(Turn.PLAYER)

        for piece in ChessBoard.chess_list:
            piece.update(delta_time)

    def render(self):
        from gameobject.chess import ChessBoard
        for piece in ChessBoard.chess_list:
            piece.render()

    def __is_end_bot_turn(self) -> bool:
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                if piece.is_end_turn is False:
                    return False
        return True

    def __handle_bot_event(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        from utils import MoveGen
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                if piece.turn_left == 0:
                    # gen move
                    pos = MoveGen.get_next_move(piece)
                    if pos == piece.current_pos:
                        continue
                    # if piece kill player
                    if pos == self.__player_position:
                        self.__is_player_killable = True
                    # promote
                    if piece.type == Type.PAWN and pos != self.__player_position and pos.y == 7:
                        piece.set_promotion(True)
                    # set move
                    piece.dest_pos = pos
                    piece.state = State.MOVING
                    piece.perform_turn()
        self.isPerforming = True
