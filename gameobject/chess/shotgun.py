from gameobject.chess.player import Player
from gameobject.sprite import Sprite


class Shotgun(Sprite):
    def __init__(self, player: Player()):
        super().__init__()
        self.__player = player
        self.__current_time = 0
        self.__bullets = []
        self.__current_ammo = 0
        self.__max_ammo = 0
        self.__current_capacity = 0
        self.__max_capacity = 0
        self.__is_shootable = False
        self.__is_shooting = False
        self.__is_finish_shoot = True
        self.__range_gun = None
        self.__range_line_l = None
        self.__range_line_r = None

    def init(self):
        from gamemanager import DATA
        self.texture = DATA.get_texture('chess/gun/shotgun')
        self.scale = (2, 2)
        self.origin = (8 * 2, 8 * 2)
        self.__is_shootable = True
        self.__is_shooting = False
        self.__is_finish_shoot = True
        #
        # m_bullets.resize(GameRule->getShotgunSpray());
        # m_maxAmmo = GameRule->getShotgunMaxAmmo();
        # m_maxCapacity = GameRule->getShotgunMaxCapacity();
        # m_currentAmmo = m_maxAmmo;
        # m_currentCapacity = m_maxCapacity;
        self.__max_ammo = 8
        self.__max_capacity = 2
        self.__current_ammo = self.__max_ammo
        self.__current_capacity = self.__max_capacity

    def sync(self):
        self.position = self.__player.position
        #
        scale_x, scale_y = self.__player.scale
        scale_x = scale_x / 3 * 2
        scale_y = scale_y / 3 * 2
        if self.scale[0] < 0:
            scale_x = -scale_x
        if self.scale[1] < 0:
            scale_y = -scale_y
        self.scale = (scale_x, scale_y)
        #
        # sf::Color
        # gunColor = this->getColor();
        # gunColor.a = m_player->getColor().a;
        # this->setColor(gunColor);

    def update(self, delta_time: float()):
        self.sync()
        from pygame import mouse
        mouse_pos = mouse.get_pos()
        if self.__is_shooting:
            self.__handle_shoot(mouse_pos, delta_time)
            return
        self.__handle_rotate_gun(mouse_pos, delta_time)
        if self.__is_shootable:
            self.__handle_draw_range(mouse_pos, delta_time)
        pass

    def render(self):
        from gamemanager import WConnect
        if self.__is_shootable and self.__is_shooting:
            # WConnect->getWindow()->draw(m_RangeGun);
            # WConnect->getWindow()->draw(m_RangeLineL);
            # WConnect->getWindow()->draw(m_RangeLineR);
            pass
        if self.__is_shooting:
            # render all bullets
            pass
        WConnect.window.blit(self.texture, self.absolute_position)
        pass

    def shoot(self):
        pass

    def set_shootable(self, value: bool):
        self.__is_shootable = value

    def reset(self):
        self.__is_shootable = True
        self.__is_shooting = False
        self.__is_finish_shoot = True
        del self.__bullets
        self.__bullets = []
        # m_bullets.resize(GameRule->getShotgunSpray());

    @property
    def finish_shoot(self) -> bool:
        return self.__is_finish_shoot

    @property
    def current_ammo(self) -> int:
        return self.__current_ammo

    @property
    def max_ammo(self) -> int:
        return self.__max_ammo

    def add_ammo(self):
        if self.__current_ammo < self.__max_ammo:
            x = min(self.__max_ammo - self.__current_ammo, self.__current_capacity)
            self.__current_ammo += x
            self.__current_capacity -= x

    @property
    def current_capacity(self) -> int:
        return self.__current_capacity

    @property
    def max_capacity(self) -> int:
        return self.__max_capacity

    def add_capacity(self):
        if self.__current_capacity < self.__max_capacity:
            self.__current_capacity += 1

    @property
    def bullets(self) -> list:
        return self.__bullets

    def __handle_shoot(self, mouse_pos, delta_time: float()):
        pass

    def __handle_rotate_gun(self, mouse_pos, delta_time: float()):
        pass

    def __handle_draw_range(self, mouse_pos, delta_time: float()):
        pass
