from gameobject.sprite import Sprite


class SoulCard(Sprite):
    def __init__(self):
        super().__init__()
        from gameobject.chess.chess_piece import Type
        self.__type = Type.NOTHING
        self.__piece_img = None
        self.__title = None

    def init(self):
        from gamemanager import DATA
        from gameobject.text import Text
        self.texture = DATA.get_texture("\\chess\\card\\B_Cardbox")
        self.size = (120, 120)
        self.origin = (60, 60)
        self.position = (1004, 373)

        self.__piece_img = Sprite()
        self.__piece_img.scale = (3, 3)
        self.__piece_img.origin = (8, 23 / 2)
        self.__piece_img.position = (self.position[0], self.position[1] - 10)

        self.__title = Text()
        self.__title.string = "SOUL"
        self.__title.set_font(DATA.get_font("Silver", 40))
        self.__title.position = (982, 280)

    def update(self, delta_time: float):
        pass

    def render(self):
        from gamemanager import WConnect
        WConnect.window.blit(self.texture, self.absolute_position)
        self.__title.render()
        if self.has_soul:
            WConnect.window.blit(self.__piece_img.texture, self.__piece_img.absolute_position)

    @property
    def piece(self):
        return self.__type

    @piece.setter
    def piece(self, value):
        if self.has_soul:
            return
        from gameobject.chess.chess_piece import Type
        from gamemanager import DATA
        self.__type = value
        name = ""
        if value == Type.QUEEN:
            name = "W_Queen"
        elif value == Type.BISHOP:
            name = "W_Bishop"
        elif value == Type.KNIGHT:
            name = "W_Knight"
        elif value == Type.ROOK:
            name = "W_Rook"
        if name != "":
            self.__piece_img.texture = DATA.get_texture("\\chess\\piece\\" + name)

    def reset(self):
        from gameobject.chess.chess_piece import Type
        self.__type = Type.NOTHING

    @property
    def is_hover(self) -> bool:
        from pygame import mouse
        if self.rect.collidepoint(mouse.get_pos()):
            return True
        return False

    @property
    def has_soul(self) -> bool:
        from gameobject.chess.chess_piece import Type
        return self.__type != Type.NOTHING
