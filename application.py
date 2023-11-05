import pygame
import game_config


class Application:
    def __init__(self):
        # Application Init
        pygame.init()
        self.screen = pygame.display.set_mode((game_config.SCREEN_WIDTH, game_config.SCREEN_HEIGHT))
        pygame.display.set_icon(pygame.image.load('./resource/texture/icon.png'))
        pygame.display.set_caption(game_config.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        from gamemanager import WConnect
        from gamestatemanager import GSM
        self.__gsm = GSM
        from gamestatemanager.state_types import StateTypes
        WConnect.window = self.screen
        self.__gsm.change_state(StateTypes.INTRO)

    def update(self, delta_time: float()):
        if self.__gsm.need_to_change_state():
            self.__gsm.perform_state_change()
        self.__gsm.active_state.update(delta_time)

    def render(self):
        self.screen.fill("black")
        self.__gsm.active_state.render()
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
