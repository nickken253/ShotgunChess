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
        self.__rotation = 0.0
        self.alpha = 255
        self.colorkey = None

    @property
    def texture(self) -> pygame.surface.Surface:
        from pygame import transform
        flip_w = False if self.__scale_w > 0 else True
        flip_h = False if self.__scale_h > 0 else True
        texture = self.__texture.copy()
        texture = transform.flip(texture, flip_w, flip_h)
        texture = transform.scale(texture, (abs(self.__scale_w) * self.__size_w, abs(self.__scale_h) * self.__size_h))
        texture = transform.rotate(texture, self.__rotation)
        if self.colorkey:
            r, g, b = self.colorkey
            a = self.alpha
            texture.fill((r, g, b, a), special_flags=pygame.BLEND_RGBA_MULT)
        else:
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
        from pygame.rect import Rect
        r = self.texture.get_rect()
        x, y = self.position
        return Rect(x, y, r.w, r.h)

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
        from math import sin, cos, sqrt, atan, radians

        def calc(w, alpha, x, y):
            if y == 0:
                y = 0.00001
            return (sqrt(x * x + y * y) * sin(alpha + atan(x / y)),
                    w * sin(alpha) + sqrt(x * x + y * y) * cos(alpha + atan(x / y)))

        flip_w = False if self.__scale_w > 0 else True
        flip_h = False if self.__scale_h > 0 else True
        scale_w, scale_h = abs(self.__scale_w), abs(self.__scale_h)
        size_w, size_h = self.__size_w * scale_w, self.__size_h * scale_h
        origin_x = (self.__size_w-self.__origin_x if flip_w else self.__origin_x) * scale_w
        origin_y = (self.__size_h-self.__origin_y if flip_h else self.__origin_y) * scale_h
        new_origin_x, new_origin_y = origin_x, origin_y
        if self.__rotation <= 90:
            new_origin_x, new_origin_y = calc(size_w, radians(self.__rotation), origin_x, origin_y)
        elif self.__rotation <= 180:
            new_origin_x, new_origin_y = calc(size_h, radians(self.__rotation-90), origin_y, size_w-origin_x)
        elif self.__rotation <= 270:
            new_origin_x, new_origin_y = calc(size_w, radians(self.__rotation-180), size_w-origin_x, size_h-origin_y)
        elif self.__rotation <= 360:
            new_origin_x, new_origin_y = calc(size_h, radians(self.__rotation-270), size_h-origin_y, origin_x)
        return self.__position_x - new_origin_x, self.__position_y - new_origin_y

    def move(self, x, y):
        self.__position_x += x
        self.__position_y += y

    def contain(self, position):
        return ((self.position[0] - self.origin[0] <= position[0] <= self.position[0] - self.origin[0] + self.size[0] *
                 self.scale[0]) and
                (self.position[1] - self.origin[1] <= position[1] <= self.position[1] - self.origin[1] + self.size[1] *
                 self.scale[1]))
