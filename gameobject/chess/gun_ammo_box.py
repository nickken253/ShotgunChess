class GunAmmoBox:
    def __init__(self):
        self.__shotgun = None
        self.__last_check_ammo = 0
        self.__last_check_capacity = 0
        self.__gun_img = None
        self.__ammo = []
        self.__capacity = []

    def init(self):
        from gameobject.sprite import Sprite
        from gamemanager import DATA
        self.__gun_img = Sprite()
        self.__gun_img.texture = DATA.get_texture("\\chess\\gun\\Shotgun")
        self.__gun_img.scale = (2, 2)

    def update(self, delta_time: float):
        if self.__shotgun is None:
            return
        from gamemanager import DATA
        if self.__shotgun.current_ammo != self.__last_check_ammo:
            for i in range(self.__shotgun.current_ammo):
                self.__ammo[i].texture = DATA.get_texture("\\chess\\gun\\bullet-filled")
            for i in range(self.__shotgun.current_ammo, len(self.__ammo)):
                self.__ammo[i].texture = DATA.get_texture("\\chess\\gun\\bullet-empty")
            self.__last_check_ammo = self.__shotgun.current_ammo
        if self.__shotgun.current_capacity != self.__last_check_capacity:
            for i in range(self.__shotgun.current_capacity):
                self.__capacity[i].texture = DATA.get_texture("\\chess\\gun\\bullet-filled")
            for i in range(self.__shotgun.current_capacity, len(self.__capacity)):
                self.__capacity[i].texture = DATA.get_texture("\\chess\\gun\\bullet-empty")
            self.__last_check_capacity = self.__shotgun.current_capacity

    def render(self):
        if self.__shotgun is None:
            return
        from gamemanager import WConnect
        for ammo in self.__ammo:
            WConnect.window.blit(ammo.texture, ammo.absolute_position)
        for ammo in self.__capacity:
            WConnect.window.blit(ammo.texture, ammo.absolute_position)
        WConnect.window.blit(self.__gun_img.texture, self.__gun_img.absolute_position)

    def set_gun(self, shotgun):
        self.__shotgun = shotgun
        self.__ammo.clear()
        self.__capacity.clear()
        from gamemanager import DATA
        from gameobject.sprite import Sprite
        for i in range(shotgun.max_ammo):
            sprite = Sprite()
            sprite.texture = DATA.get_texture("\\chess\\gun\\bullet-filled")
            sprite.position = (390 + 17*i, 30)
            self.__ammo.append(sprite)
        for i in range(shotgun.max_capacity):
            sprite = Sprite()
            sprite.texture = DATA.get_texture("\\chess\\gun\\bullet-filled")
            sprite.position = (390 + 17*i, 30 + 30)
            self.__capacity.append(sprite)
        self.__last_check_ammo = len(self.__ammo)
        self.__last_check_capacity = len(self.__capacity)
        self.__gun_img.position = (self.__ammo[-1].position[0] + 15, self.__ammo[-1].position[1] - 5)
