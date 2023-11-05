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
        self.alpha = 255

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
        texture.set_alpha(self.alpha)
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
        return self.__position_x - self.__origin_x * self.__scale_w, self.__position_y - self.__origin_y * self.__scale_h

    def move(self, x, y):
        self.__position_x += x
        self.__position_y += y

    def contain(self, position):
        return ((self.position[0] - self.origin[0] <= position[0] <= self.position[0] - self.origin[0] + self.size[0] *
                 self.scale[0]) and
                (self.position[1] - self.origin[1] <= position[1] <= self.position[1] - self.origin[1] + self.size[1] *
                 self.scale[1]))