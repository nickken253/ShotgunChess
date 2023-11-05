from gameturn.game_turn import Base


class ShowupTurn(Base):
    def __init__(self):
        super().__init__()
        self.__current_time = 0

    def init(self):
        from gameobject.chess import ChessBoard
        ChessBoard.player.gun.set_shootable(False)
        for piece in ChessBoard.chess_list:
            piece.perform_turn()
        self.isPerforming = False
        self.__current_time = 0

    def __handle_player_show_up(self, delta_time: float()):
        from gameobject.chess import ChessBoard
        ChessBoard.player.update(delta_time)

    def __handle_bot_show_up(self, delta_time: float()):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type
        from game_config import SHOW_UP_DURATION
        self.__current_time += delta_time
        n_piece = len(ChessBoard.chess_list) - 1
        i = 0
        end_count = 0
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                if self.__current_time >= SHOW_UP_DURATION / 2 * i:
                    piece.update(delta_time)
                    if piece.is_end_turn:
                        end_count += 1
                i += 1
        if end_count == n_piece:
            self.isPerforming = True

    def update(self, delta_time: float()):
        from gameobject.chess import ChessBoard
        from gameturn import GTM
        from gameturn.game_turn import Turn
        if self.isPerforming is False:
            self.__handle_player_show_up(delta_time)
            if ChessBoard.player.is_end_turn:
                self.__handle_bot_show_up(delta_time)
        else:
            ChessBoard.player.update(delta_time)
            ChessBoard.enable()
            GTM.change_turn(Turn.PLAYER)

    def render(self):
        from gameobject.chess import ChessBoard
        for piece in ChessBoard.chess_list:
            piece.render()
        # ChessBoard.render()
