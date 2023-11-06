from gameturn.game_turn import Base


class LoseTurn(Base):
    def __init__(self):
        super().__init__()
        self.__piece = None
        self.__current_time = 0
        self.__background = None
        self.__alpha_color = 0
        self.__btn_back = None

    def init(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        from gameobject.game_button import GameButton
        from gameobject.sprite import Sprite
        from gamemanager import DATA
        from game_config import SCREEN_WIDTH, SCREEN_HEIGHT
        from gameturn import GTM
        player_pos = ChessBoard.player.current_pos
        for piece in ChessBoard.chess_list:
            if piece != Type.PLAYER:
                if piece.turn_left == 0 and piece.dest_pos == player_pos:
                    self.__piece = piece
                    continue
                piece.state = State.IDLE
                piece.is_end_turn = True

        self.__btn_back = GameButton("btnBackToMenu", (262, 64))
        self.__btn_back.position = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 75)
        self.__btn_back.set_on_click(self.__btn_back_on_click)
        self.__btn_back.init()

        self.__background = Sprite()
        self.__background.texture = DATA.get_texture("bg-dead")
        self.__background.position = (0, 0)
        self.__background.alpha = 0
        self.__alpha_color = 0
        self.__update_color()

        self.isPerforming = True
        self.__current_time = 0

        GTM.reset_count()

    def update(self, delta_time: float()):
        if self.isPerforming:
            self.__handle_kill_event(delta_time)
        else:
            self.__handle_after_death(delta_time)

    def render(self):
        from gameobject.chess import ChessBoard
        from gamemanager import WConnect
        for piece in ChessBoard.chess_list:
            piece.render()
        if self.isPerforming is False:
            WConnect.window.blit(self.__background.texture, self.__background.absolute_position)
            self.__btn_back.render()

    def __update_color(self):
        self.__background.alpha = self.__alpha_color
        self.__btn_back.alpha = self.__alpha_color

    def __handle_kill_event(self, delta_time: float):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import State
        self.__piece.update(delta_time)
        ChessBoard.player.update(delta_time)
        if ChessBoard.player.state == State.IDLE and self.__piece.rect.colliderect(ChessBoard.player.rect):
            ChessBoard.player.shoot_pos = self.__piece.current_pos
            ChessBoard.player.state = State.KILL
            ChessBoard.player.perform_turn()
        if ChessBoard.player.state == State.DEAD and ChessBoard.player.is_end_turn:
            self.isPerforming = False
            ChessBoard.disable()
            # DATA->playSound("smb_gameover");


    def __handle_after_death(self, delta_time: float):
        self.__current_time += delta_time
        from game_config import TRANSITION_DURATION
        if self.__current_time < TRANSITION_DURATION * 2:
            self.__alpha_color = min(255, int(round(255*self.__current_time/(TRANSITION_DURATION*2))))
        else:
            self.__alpha_color = 255
            self.__btn_back.update(delta_time)
        self.__update_color()

    def __btn_back_on_click(self):
        from gamestatemanager import GSM
        GSM.pop_state()
        GSM.pop_state()
