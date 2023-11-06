import pygame.surface

from gamemanager import DATA, WConnect
from gameobject.sprite import Sprite


class GameButton(Sprite):
    def __init__(self, name, size):
        super().__init__()
        self.btn_click_func = None
        self.is_handling = False
        self.btn_name = name
        self.size = size
        self.origin = (size[0] / 2, size[1] / 2)
        self.sound_played = False

    def __del__(self):
        pass

    def init(self):
        self.texture = DATA.get_texture("\\gui\\" + self.btn_name + "_idle")

    def update(self, delta_time: float):
        if self.contain(pygame.mouse.get_pos()):
            self.texture = DATA.get_texture("\\gui\\" + self.btn_name + "_handle")
            if not self.sound_played:
                DATA.play_sound("hover")
                self.sound_played = True
            if pygame.mouse.get_pressed()[0]:
                DATA.play_sound("click")
                self.btn_click_func()
                self.is_handling = True
        else:
            self.texture = DATA.get_texture("\\gui\\" + self.btn_name + "_idle")
            self.is_handling = False
            self.sound_played = False

    def render(self):
        WConnect.window.blit(self.texture, self.absolute_position)

    def is_handle(self):
        return self.is_handling

    def set_on_click(self, on_click):
        self.btn_click_func = on_click
