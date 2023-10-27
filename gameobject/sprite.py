import math

import pygame.surface


class Sprite:
    def __init__(self):
        self.__texture = None
        self.__position_x = 0
        self.__position_y = 0
        self.__origin_x = 0
        self.__origin_y = 0
        self.__size_w = 0
        self.__size_h = 0
        self.__scale_w = 1
        self.__scale_h = 1
        self.__rotation = 0

    @property
    def texture(self) -> pygame.surface.Surface:
        from pygame import transform
        flip_w, flip_h = False, False
        if self.__scale_w < 0:
            flip_w = True
        if self.__scale_h < 0:
            flip_h = True
        texture = transform.flip(self.__texture, flip_w, flip_h)
        texture = transform.scale(texture, (abs(self.__scale_w) * self.__size_w, abs(self.__scale_h) * self.__size_h))
        texture = transform.rotate(texture, self.__rotation)
        return texture

    @texture.setter
    def texture(self, value):
        self.__texture = value
        self.__size_w, self.__size_h = value.get_rect().size

    @property
    def size(self):
        return self.__size_w, self.__size_h

    @size.setter
    def size(self, value):
        from pygame.transform import scale
        if self.__texture:
            self.texture = scale(self.__texture, value)

    @property
    def scale(self):
        return self.__scale_w, self.__scale_h

    @scale.setter
    def scale(self, value):
        self.__scale_w, self.__scale_h = value

    @property
    def rotation(self) -> float:
        return self.__rotation

    @rotation.setter
    def rotation(self, value):
        self.__rotation = value
        if value >= 360:
            self.__rotation -= 360

    @property
    def rect(self) -> pygame.rect.Rect:
        if self.__texture is None:
            from pygame.rect import Rect
            x, y = self.position
            w, h = self.size
            return Rect(x, y, w, h)
        else:
            return self.__texture.get_rect()

    @property
    def position(self):
        return self.__position_x, self.__position_y

    @position.setter
    def position(self, value):
        self.__position_x, self.__position_y = value

    @property
    def origin(self):
        return self.__origin_x, self.__origin_y

    @origin.setter
    def origin(self, value):
        self.__origin_x, self.__origin_y = value

    @property
    def absolute_position(self):
        x, y = self.__position_x, self.__position_y
        angle = math.radians(self.__rotation)
        origin_x = self.__origin_x * math.cos(angle) - self.__origin_y * math.sin(angle)
        origin_y = self.__origin_x * math.sin(angle) + self.__origin_y * math.cos(angle)
        if self.__rotation <= 90:
            angle = math.radians(self.__rotation)
            y -= self.__size_w * math.sin(angle)
        elif self.__rotation <= 180:
            angle = math.radians(self.__rotation - 90)
            y -= self.__size_h * math.sin(angle) + self.__size_w * math.cos(angle)
            x -= self.__size_w * math.sin(angle)
        return self.__position_x - origin_x, self.__position_y - origin_y

    def move(self, x, y):
        self.__position_x += x
        self.__position_y += y
