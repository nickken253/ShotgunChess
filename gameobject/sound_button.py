import pygame.mouse

from gamemanager import DATA, WConnect
from gameobject.sprite import Sprite


class SoundButton(Sprite):
    def __init__(self):
        super().__init__()
        self.is_handling = False
        self.current_time = 0.0
        self.sound = None

    def __del__(self):
        pass

    def init(self):
        if DATA.is_enable_sound():
            self.texture = DATA.get_texture("\\gui\\btnSound_enable")
        else:
            self.texture = DATA.get_texture("\\gui\\btnSound_disable")
        self.size = (15.0, 13.0)
        self.scale = (3.0, 3.0)
        self.position = (10, 10)
        self.is_handling = False
        self.current_time = 0.0
        self.sound = True

    def update(self, delta_time: float):
        if self.is_handling:
            self.current_time += delta_time
            if self.current_time > 0.25:
                self.current_time = 0.0
                self.is_handling = False
            return
        if self.contain(pygame.mouse.get_pos()):
            from gamemanager import DATA
            if pygame.mouse.get_pressed()[0]:
                self.is_handling = True
                self.sound = not self.sound
                if  self.sound:
                    # DATA.play_sound("click")
                    self.texture = DATA.get_texture("\\gui\\btnSound_enable")
                    DATA.enable_sound()
                    DATA.unpause_sound("ingame")
                else:
                    self.texture = DATA.get_texture("\\gui\\btnSound_disable")
                    DATA.disable_sound()
                    DATA.pause_sound("ingame")
            else:
                self.is_handling = False

    def render(self):
        WConnect.window.blit(self.texture, self.absolute_position)
        pass
