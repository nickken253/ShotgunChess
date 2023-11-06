from gameobject.chess.chess_position import ChessPosition
from gameobject.rectangle import Rectangle
from gameobject.sprite import Sprite


class ChessBox(Rectangle):
    def __init__(self, size, chess_pos: ChessPosition()):
        super().__init__((0, 0), size, (0, 0, 0, 0), (255, 0, 0))
        self.size = size
        self.__chess_pos = chess_pos
        self.rect.x, self.rect.y = chess_pos.position
        self.origin = (self.rect.w / 2, self.rect.h / 2 - 23/2 - 5)  # Magic offset number
        # Outline init
        self.__outline = Sprite()
        from gamemanager import DATA
        self.__outline.texture = DATA.get_texture("\chess\MoveBox")
        self.__outline.origin = (45, 45)
        x, y = self.rect.x, self.rect.y
        self.__outline.position = (x, y + 23 / 2 + 4.7)  # Magic offset number
        self.__is_visible = False

    @property
    def is_mouse_hover(self) -> bool:
        from pygame import mouse
        return self.absolute_rect.collidepoint(mouse.get_pos())

    @property
    def is_mouse_click(self) -> bool:
        from pygame import mouse
        return mouse.get_pressed()[0] and self.is_mouse_hover

    @property
    def chess_position(self) -> ChessPosition:
        return self.__chess_pos

    def render(self):
        if self.__is_visible:
            from gamemanager import WConnect
            # super().render()
            WConnect.window.blit(self.__outline.texture, self.__outline.absolute_position)

    def showOutline(self):
        self.__is_visible = True

    def hideOutline(self):
        self.__is_visible = False
