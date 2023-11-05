from gamemanager import WConnect, DATA
from gamestatemanager.game_state_base import GameStateBase
from gamestatemanager import GSM


class GSEnd(GameStateBase):
    def __init__(self):
        super().__init__()
        self.background = None
        self.alpha_color = None
        self.btn_back = None
        self.current_time = 0.0

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
        self.current_time = 0.0
        self.background = DATA.get_texture("bg-end")
        from gameobject.game_button import GameButton
        self.btn_back = GameButton("btnBackToMenu", (262.0, 64.0))
        self.btn_back.init()
        import game_config
        self.btn_back.position = (game_config.SCREEN_WIDTH / 2, game_config.SCREEN_HEIGHT / 2 + 250.0)
        self.btn_back.set_on_click(lambda: (
            GSM.pop_state(),
            GSM.pop_state(),
            GSM.pop_state()
        ))
        DATA.play_sound("smb_stage_clear")

    def update(self, delta_time: float):
        super().update(delta_time)
        import game_config
        self.current_time += delta_time
        if self.current_time < game_config.TRANSITION_DURATION * 2:
            pass
        else:
            self.btn_back.update(delta_time)

    def render(self):
        super().render()
        WConnect.get_window().blit(self.background, (0, 0))
        self.btn_back.render()

    def update_color(self):
        pass
