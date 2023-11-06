import pygame.font


class Text:
    def __init__(self, color=(255, 255, 255)):
        self.font = None
        self.position = (0, 0)
        self.origin = (0, 0)
        self.string = ""
        self.color = color

    @property
    def absolute_position(self):
        return self.position[0] - self.origin[0], self.position[1] - self.origin[1]

    @property
    def surface(self):
        return self.font.render(self.string, True, self.color)

    def render(self):
        from gamemanager import WConnect
        WConnect.window.blit(self.surface, self.absolute_position)

    def set_font(self, font):
        self.font = font
