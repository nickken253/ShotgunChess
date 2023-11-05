import math


class Bullet:
    def __init__(self):
        from gameobject.line import Line
        self.__current_time = 0
        self.__is_flying = False
        self.__is_visible = False
        self.__angle = 0
        self.__shoot_pos = (0, 0)
        self.__bullet_line = Line()

    def init(self, pos, angle):
        self.__angle = angle
        self.__shoot_pos = pos
        self.__is_flying = True
        self.__is_visible = True
        self.__bullet_line.color = (255, 0, 0)
        self.__bullet_line.start_pos = pos
        self.__bullet_line.end_pos = pos

    def update(self, delta_time: float):
        from gameobject import GRM
        from game_config import SHOOTING_DURATION
        self.__current_time += delta_time
        r = GRM.shot_gun_range * 2 / 3
        velocity = SHOOTING_DURATION / r
        if self.__current_time < SHOOTING_DURATION / 2:
            if self.__is_flying:
                offset = r * (self.__current_time / (SHOOTING_DURATION / 2))
                self.__bullet_line.end_pos = (
                    self.__shoot_pos[0] + offset * math.cos(self.__angle),
                    self.__shoot_pos[1] + offset * math.sin(self.__angle)
                )
        elif self.__current_time < SHOOTING_DURATION:
            offset = r * (self.__current_time / (SHOOTING_DURATION / 2) - 1)
            self.__bullet_line.start_pos = (
                self.__shoot_pos[0] + offset * math.cos(self.__angle),
                self.__shoot_pos[1] + offset * math.sin(self.__angle)
            )
        else:
            self.__is_visible = False
            self.__is_flying = False
            self.__current_time = 0

    def render(self):
        self.__bullet_line.render()

    def get_hitbox(self):
        return self.__bullet_line.end_pos

    @property
    def is_flying(self) -> bool:
        return self.__is_flying

    def stop(self):
        self.__is_flying = False

    def get_damage(self) -> int:
        from utils import GMath
        from gameobject import GRM
        r = GMath.get_distance(self.__shoot_pos, self.__bullet_line.end_pos)
        damage = int(round(GRM.shot_gun_damage * (1 - r / GRM.shot_gun_range)))
        if damage < 0:
            damage = 0
        elif damage > GRM.shot_gun_damage:
            damage = GRM.shot_gun_damage
        return damage
