import pygame
import game_config

class Application:
    def __init__(self):
        # Application Init
        pygame.init()
        self.screen = pygame.display.set_mode((game_config.SCREEN_WIDTH, game_config.SCREEN_HEIGHT))
        from gamemanager import WConnect
        WConnect.window = self.screen
        pygame.display.set_icon(pygame.image.load('./resource/texture/icon.png'))
        pygame.display.set_caption('ShotgunChess - Nhom 7')
        self.clock = pygame.time.Clock()
        self.running = True
        # Modules init
        from gameturn import game_turn_machine
        from gameturn.game_turn import Turn
        self.__gtm = game_turn_machine
        self.__gsm = None
        self.__gtm.change_turn(Turn.PLAYER)

    def update(self, delta_time: float()):
        if self.__gtm.need_to_change_turn:
            self.__gtm.perform_change()
        self.__gtm.current_turn.update(delta_time)

    def render(self):
        self.screen.fill("black")
        self.__gtm.current_turn.render()
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            delta_time = self.clock.tick(game_config.FRAMERATE_LIMIT) / 1000
            self.update(delta_time)
            self.render()
        pygame.quit()


application = Application()
application.run()
