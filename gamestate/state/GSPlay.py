from gamemanager import WConnect, DATA
from gamestate.game_state_base import GameStateBase
from gamestate import GSM


class GSPlay(GameStateBase):
    def __init__(self):
        super().__init__()
        self.background = None
        self.current_time = 0.0
        self.is_perform_transition = True
        self.home_btn = None
        self.sound_btn = None

    def __del__(self):
        pass

    def exit(self):
        super().exit()

    def pause(self):
        super().pause()

    def resume(self):
        super().resume()

    def init(self):
        super().init()
        import game_config

        from gameobject.sound_button import SoundButton
        self.sound_btn = SoundButton()
        self.sound_btn.init()

        from gameobject.game_button import GameButton
        self.home_btn = GameButton("btnHome", (16.0, 16.0))
        self.home_btn.init()
        self.home_btn.scale = (3.0, 3.0)
        self.home_btn.origin = (8, 8)
        self.home_btn.position = (game_config.SCREEN_WIDTH - 16 - 10.0, 16 + 10.0)
        self.home_btn.set_on_click(self.__home_btn_on_click)

        self.current_time = 0.0
        self.is_perform_transition = True

        from gameobject.chess import ChessBoard
        ChessBoard.init()
        ChessBoard.set_level(1)

        self.background = DATA.get_texture("bg")
        self.background.set_alpha(150)

    def update(self, delta_time: float):
        super().update(delta_time)
        self.sound_btn.update(delta_time)
        self.home_btn.update(delta_time)
        from gameobject.chess import ChessBoard
        ChessBoard.update(delta_time)

    def render(self):
        super().render()
        WConnect.window.blit(self.background, (0, 0))
        self.sound_btn.render()
        self.home_btn.render()
        from gameobject.chess import ChessBoard
        ChessBoard.render()

    def __home_btn_on_click(self):
        GSM.pop_state()
        GSM.pop_state()
        pass
