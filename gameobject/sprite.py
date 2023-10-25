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

    @property
    def texture(self) -> pygame.surface.Surface:
        return self.__texture

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

    def set_scale(self, value):
        scale_w, scale_h = value
        w, h = self.size
        self.size = (w*scale_w, h*scale_h)

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
        return self.__position_x - self.__origin_x, self.__position_y - self.__origin_y

    def move(self, x, y):
        self.__position_x += x
        self.__position_y += y
