class Text:
    def __init__(self, color=(255, 255, 255)):
        self.font = None
        self.surface = None
        self.position = (0, 0)
        self.string = ""
        self.color = color

    def render(self):
        from gamemanager import WConnect
        WConnect.get_window().blit(self.surface, self.position)

    def set_font(self, font):
        self.font = font
        self.surface = self.font.render(self.string, True, self.color)
