from gamemanager.singleton import Singleton
from gameobject.chess.chess_piece import ChessPiece
from gameobject.chess.player import Player
from gameobject.sprite import Sprite


class Board(Sprite, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.__is_enabled = False
        self.__player = None
        self.__chess_list = []
        from gameobject.chess.chess_position import ChessPosition
        from gameobject.chess.chess_box import ChessBox
        self.__chess_table = [[ChessBox((64.5, 64.5), ChessPosition(x, y)) for x in range(8)] for y in range(8)]
        self.__soul_card = None
        self.__info_box = None
        self.__gun_ammo_box = None
        self.__cash_counter = None
        self.__rot = 0

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
        from gameturn import GTM
        if GTM.need_to_change_turn:
            GTM.perform_change()
        GTM.current_turn.update(delta_time)
        if self.__is_enabled is False:
            return
        # m_soulCard->update(deltaTime);
        # m_ammoBox->update(deltaTime);
        self.__info_box.update(delta_time)
        pass

    def render(self):
        from gamemanager import WConnect
        WConnect.window.blit(self.texture, self.absolute_position)
        WConnect.window.blit(self.texture, self.absolute_position)
        from gameturn import GTM
        GTM.current_turn.render()
        for y in range(8):
            for x in range(8):
                self.__chess_table[y][x].render()
        if not self.__is_enabled:
            return
        # m_soulCard->render();
        # m_ammoBox->render();
        self.__info_box.render()
        # draw chess box
        for y in range(8):
            for x in range(8):
                self.__chess_table[y][x].render()


    def set_level(self, level: int()):
        # Clear board
        from gameobject import GRM
        from gameobject.chess.chess_piece import Type
        self.__chess_list.clear()
        self.__chess_list = GRM.get_chess_list(level)
        for piece in self.__chess_list:
            if piece.type == Type.PLAYER:
                self.__player = piece
                break
        # //
        #     if (m_soulCard == nullptr) {
        #         m_soulCard = new SoulCard();
        #         m_soulCard->init();
        #     }
        if self.__info_box is None:
            from gameobject.chess.info_box import InfoBox
            self.__info_box = InfoBox()
            self.__info_box.init()
        #     if (m_ammoBox == nullptr) {
        #         m_ammoBox = new GunAmmoBox();
        #         m_ammoBox->init();
        #     }
        #     if (level == 1) CCounter->reset();
        #     //
        #     m_soulCard->reset();
        #     m_ammoBox->setGun(m_player->getGun());
        from gameturn import GTM
        from gameturn.game_turn import Turn
        GTM.change_turn(Turn.SHOW_UP)
        pass

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def chess_list(self) -> list[ChessPiece]:
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
