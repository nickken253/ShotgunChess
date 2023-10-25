from gameobject.chess.player import Player
from gameobject.sprite import Sprite


class Board(Sprite):
    def __init__(self):
        super().__init__()
        self.__is_enabled = False
        self.__player = None
        self.__chess_list = None
        from gameobject.chess.chess_position import ChessPosition
        from gameobject.chess.chess_box import ChessBox
        self.__chess_table = [[ChessBox((64.5, 64.5), ChessPosition(x, y)) for x in range(8)] for y in range(8)]
        self.__soul_card = None
        self.__info_box = None
        self.__gun_ammo_box = None
        self.__cash_counter = None

    def init(self):
        from pygame import image
        self.__is_enabled = True
        self.texture = image.load('resource/texture/chess/Board.png')
        self.size = (550, 550 + 6)
        self.origin = (550 / 2, 550 / 2)
        self.position = (640, 373)
        from gameobject.chess.chess_position import ChessPosition
        self.__cash_counter = None  # init

        self.__player = Player()
        self.__player.init(ChessPosition(3, 7))

    def update(self, delta_time: float()):
        new_x = delta_time * 5
        new_y = 0
        # self.__player.move(new_x, 0)
        pass

    def render(self):
        from application import application
        application.screen.blit(self.texture, self.absolute_position)
        self.__player.render()
        # GTM->currentTurn()->render();
        for y in range(8):
            for x in range(8):
                self.__chess_table[y][x].render()

        if not self.__is_enabled:
            return
        # m_soulCard->render();
        # m_infoBox->render();
        # m_ammoBox->render();
        # for (int y = 0; y < 8; y++) {
            # for (int x = 0; x < 8; x++) {
            #    m_ChessTable[y][x].render();
            # }
        # }

    def set_level(self, level: int()):
        pass

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def chess_list(self):
        return self.__chess_list

    def get_check_box(self, x: int(), y: int()):
        return self.__chess_table[y][x]

    @property
    def soul_card(self):
        return self.__soul_card

    def disable(self):
        self.__is_enabled = False

    def enable(self):
        self.__is_enabled = True
