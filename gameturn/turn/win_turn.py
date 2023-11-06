from gameturn.game_turn import Base


class WinTurn(Base):
    def __init__(self):
        super().__init__()
        self.__player_pos = None

    def init(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        from gameturn import GTM
        ChessBoard.player.gun.set_shootable(False)
        self.__player_pos = ChessBoard.player.current_pos
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                piece.shoot_pos = self.__player_pos
                piece.state = State.KILL
                piece.perform_turn()

        GTM.reset_count()

    def update(self, delta_time: float()):
        from gameobject.chess import ChessBoard
        from gameobject import GRM
        from gamestatemanager import GSM
        from gamestatemanager.state_types import StateTypes
        from game_config import FINAL_LEVEL
        if len(ChessBoard.chess_list) == 1:
            if GRM.current_level == FINAL_LEVEL:
                GSM.change_state(StateTypes.END)
            else:
                GSM.change_state(StateTypes.UPGRADE)
        for piece in ChessBoard.chess_list:
            piece.update(delta_time)
        self.__handle_clear_board()
        pass

    def render(self):
        from gameobject.chess import ChessBoard
        for piece in ChessBoard.chess_list:
            piece.render()

    def __handle_clear_board(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import State
        i = 0
        while i < len(ChessBoard.chess_list):
            if ChessBoard.chess_list[i].state == State.DEAD:
                ChessBoard.chess_list.pop(i)
                i -= 1
            i += 1
