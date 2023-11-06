import os

import pygame

from gamemanager.singleton import Singleton


class ResourceManager(metaclass=Singleton):
    def __init__(self):
        self.isPreloaded = None
        self.isSoundEnable = True
        self.map_texture = {}
        self.map_font = {}
        self.map_sound = {}
        self.custom_cursor = None
        self.path = os.path.join(os.path.dirname(__file__), '..', 'resource')
        self.texture_path = self.path + "\\texture"
        self.font_path = self.path + "\\font"
        self.sound_path = self.path + "\sound"

    def __del__(self):
        self.map_texture.clear()

    def add_texture(self, name: str):
        # print("" + self.texture_path + "\\" + name + ".png")
        texture = pygame.image.load(self.texture_path + "\\" + name + ".png").convert_alpha()
        if name in self.map_texture:
            return
        self.map_texture[name] = texture

    def remove_texture(self, name: str):
        if name in self.map_texture:
            del self.map_texture[name]

    def get_texture(self, name: str):
        if name in self.map_texture:
            return self.map_texture[name]
        self.add_texture(name)
        return self.get_texture(name).copy()

    def has_texture(self, name: str) -> bool:
        return name in self.map_texture

    def add_font(self, name: str, size: int):
        # print("" + self.font_path + "\\" + name + ".ttf")
        font = pygame.font.Font(self.font_path + "\\" + name + ".ttf", size)
        font_key = f"{name}_{size}"
        if font_key in self.map_font:
            return
        self.map_font[font_key] = font


    def remove_font(self, name: str, size: int):
        key = f"{name}_{size}"
        if key in self.map_font:
            del self.map_font[key]

    def get_font(self, name: str, size: int):
        key = f"{name}_{size}"
        if key in self.map_font:
            return self.map_font[key]
        self.add_font(name, size)
        return self.get_font(name, size)

    def has_font(self, name: str, size: int) -> bool:
        key = f"{name}_{size}"
        return key in self.map_font

    def add_sound(self, name):
        # print("" + self.sound_path + "\\" + name + ".wav")
        sound = pygame.mixer.Sound(self.sound_path + "\\" + name + ".wav")
        if name in self.map_sound:
            return
        self.map_sound[name] = sound


    def remove_sound(self, name):
        if name in self.map_sound:
            del self.map_sound[name]

    def get_sound(self, name):
        if name in self.map_sound:
            return self.map_sound[name]
        self.add_sound(name)
        return self.get_sound(name)

    def has_sound(self, name):
        return name in self.map_sound

    def play_sound(self, name):
        if self.is_enable_sound():
            # print(f"Play sound: {name}")
            self.get_sound(name).play()
        else:
            print(f"Sound is disabled")
        
    def stop_sound(self, name):
        self.get_sound(name).stop()
        
    def pause_sound(self, name):
        self.get_sound(name).set_volume(0)
        
    def unpause_sound(self, name):
        self.get_sound(name).set_volume(100)
        
    def set_cursor(self, name):
        if self.custom_cursor is not None:
            self.custom_cursor = None
        self.custom_cursor = pygame.image.load(os.path.join(self.texture_path, name + ".png")).convert_alpha()

    def preload(self):
        if self.isPreloaded:
            return

        self.add_font("Silver", 12)

        sound_list = [
            "cash",
            "drop1",
            "drop2",
            "drop3",
            "shoot",
            "smb_gameover",
            "smb_stage_clear",
        ]
        for sound in sound_list:
            self.add_sound(sound)

        texture_list = [
            "bg-about",
            "bg-dead",
            "bg-end",
            "bg",
            "bg2",
            "intro",
            "logo",
            "chess\Board",
            "chess\CashCounter",
            "chess\MoveBox",
            "chess\card\B_Cardbox",
            "chess\card\W_Cardbox",
            "chess\gun\Bullet-empty",
            "chess\gun\Bullet-filled",
            "chess\gun\Shotgun",
            "chess\piece\B_Bishop",
            "chess\piece\B_King",
            "chess\piece\B_Knight",
            "chess\piece\B_Pawn",
            "chess\piece\B_Queen",
            "chess\piece\B_Rook",
            "chess\piece\W_Bishop",
            "chess\piece\W_King",
            "chess\piece\W_Knight",
            "chess\piece\W_Pawn",
            "chess\piece\W_Queen",
            "chess\piece\W_Rook",
            "cursor\point",
            "cursor\shoot",
            "cursor\\target",
            "gui\\btnAbout_handle",
            "gui\\btnAbout_idle",
            "gui\\btnBackToMenu_handle",
            "gui\\btnBackToMenu_idle",
            "gui\\btnContinue_handle",
            "gui\\btnContinue_idle",
            "gui\\btnEasy_handle",
            "gui\\btnEasy_idle",
            "gui\\btnExit_handle",
            "gui\\btnExit_idle",
            "gui\\btnHard_handle",
            "gui\\btnHard_idle",
            "gui\\btnHome_handle",
            "gui\\btnHome_idle",
            "gui\\btnMenu_handle",
            "gui\\btnMenu_idle",
            "gui\\btnNormal_handle",
            "gui\\btnNormal_idle",
            "gui\\btnPlay_handle",
            "gui\\btnPlay_idle",
            "gui\\btnSound_disable",
            "gui\\btnSound_enable",
            "gui\shopBoard",
        ]
        for texture in texture_list:
            if not self.has_texture(texture):
                self.add_texture(texture)
        self.isPreloaded = True
    def is_enable_sound(self) -> bool:
        return self.isSoundEnable

    def enable_sound(self):
        self.isSoundEnable = True

    def disable_sound(self):
        self.isSoundEnable = False
