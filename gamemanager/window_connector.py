import pygame.surface


class WindowConnector:
    def __init__(self):
        self.__window = None

    @property
    def window(self) -> pygame.surface.Surface:
        return self.__window

    @window.setter
    def window(self, value: pygame.surface.Surface):
        self.__window = value
