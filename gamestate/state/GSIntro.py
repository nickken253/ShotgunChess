from gamemanager import WConnect, DATA
from gamestate import GSM
from gamestate.game_state_base import GameStateBase
from gamestate.state_types import StateTypes


class GSIntro(GameStateBase):
    def __init__(self):
        super().__init__()
        self.logo = None
        self.alpha = None
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
        self.logo = DATA.get_texture("intro")
        DATA.play_sound("intro")
        self.alpha = 0

    def update(self, delta_time: float):
        super().update(delta_time)
        self.current_time += delta_time
        if self.current_time <= 1.0:
            self.alpha = min(255, round(self.current_time * 255))
        elif self.current_time <= 2.0:
            DATA.preload()
            self.alpha = 255
        elif self.current_time <= 3.0:
            self.alpha = max(0, round((3.0 - self.current_time) * 255))
        else:
            GSM.change_state(StateTypes.MENU)
        self.logo.set_alpha(self.alpha)

    def render(self):
        super().render()
        WConnect.window.blit(self.logo, (0, 0))

    def update_color(self):
        pass
