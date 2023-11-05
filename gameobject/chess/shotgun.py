from gameobject.sprite import Sprite


class Shotgun(Sprite):
    def __init__(self, player):
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
        self.texture = DATA.get_texture("\\chess\\gun\\shotgun")
        self.scale = (2, 2)
        self.origin = (8, 8)
        self.__is_shootable = True
        self.__is_shooting = False
        self.__is_finish_shoot = True
        #
        # m_bullets.resize(GameRule->getShotgunSpray());
        from gameobject import GRM
        self.__max_ammo = GRM.shot_gun_max_ammo
        self.__max_capacity = GRM.shot_gun_max_capacity
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
        color_a = self.__player.alpha
        self.alpha = color_a

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
        pos = self.position
        # for (int i = 0; i < GameRule->getShotgunSpray(); i++) {
        # 		Bullet* bullet = new Bullet();
        # 		float angle = this->getRotation();
        # 		int range = SHOOTING_RANGE_ANGLE*7/9;
        # 		angle = angle + GameMath::getRandom(-range / 2, range / 2);
        # 		angle = GameMath::degreeToRad(angle);
        # 		pos.x += 8.f * cos(angle);
        # 		pos.y += 8.f * sin(angle);
        # 		bullet->init(pos, angle);
        # 		if (m_bullets[i] != nullptr) delete m_bullets[i];
        # 		m_bullets[i] = bullet;
        # 	}
        self.__current_ammo -= 1
        self.__is_finish_shoot = False
        self.__is_shooting = True

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
        self.__current_time = 0
        self.__is_shooting = False
        self.__is_shootable = False
        self.__is_finish_shoot = True
        self.__player.is_end_turn = True
        pass

    def __handle_rotate_gun(self, mouse_pos, delta_time: float()):
        from utils import GMath
        from math import pi
        angle = GMath.rad_to_degree(
            2*pi - GMath.get_angle(self.position, mouse_pos)
        )
        self.rotation = angle
        if angle < 90 or angle > 270:
            self.scale = (2, 2)
        else:
            self.scale = (2, -2)
        pass

    def __handle_draw_range(self, mouse_pos, delta_time: float()):
        pass
