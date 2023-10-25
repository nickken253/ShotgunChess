from gameobject.sprite import Sprite


class Shotgun(Sprite):
    def __init__(self):
        super().__init__()
        self.__player = None
        self.__current_time = 0
        self.__bullets = []
        self.__max_ammo = 0
        self.__current_capacity = 0
        self.__max_capacity = 0
        self.__is_shootable = False
        self.__is_shooting = False
        self.__is_finish_shoot = False
        self.__range_gun = None
        self.__range_line_l = None
        self.__range_line_r = None

    def init(self):
        pass

    def sync(self):
        pass

    def update(self, delta_time: float()):
        pass

    def render(self):
        pass

    def shoot(self):
        pass

    def set_shootable(self, value: bool):
        pass

    def reset(self):
        pass

    def finish_shoot(self):
        pass

    @property
    def current_ammo(self) -> int:
        pass

    @property
    def max_ammo(self) -> int:
        pass

    def add_ammo(self):
        pass

    @property
    def current_capacity(self) -> int:
        pass

    @property
    def max_capacity(self) -> int:
        pass

    def add_capacity(self):
        pass

    @property
    def bullets(self) -> list:
        pass
