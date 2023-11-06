class InfoBox:
    def __init__(self):
        self.__health_lbl = None
        self.__turn_lbl = None
        self.__gun_info_list = []
        self.__is_display = False
        pass

    def init(self):
        from gameobject.text import Text
        from gamemanager import DATA
        self.__health_lbl = Text()
        self.__turn_lbl = Text()
        self.__health_lbl.set_font(DATA.get_font("Silver", 36))
        self.__turn_lbl.set_font(DATA.get_font("Silver", 36))
        self.__health_lbl.position = (245, 300)
        self.__turn_lbl.position = (245, 350)

        self.__gun_info_list.clear()
        for i in range(6):
            text = Text()
            text.set_font(DATA.get_font("Silver", 36))
            if i == 0:
                text.string = "RANGE"
            elif i == 2:
                text.string = "DAMAGE"
            elif i == 4:
                text.string = "PELLET"
            self.__gun_info_list.append(text)
        for i in range(6):
            offset = 40*i
            if i % 2 != 0:
                offset -= 7
            self.__gun_info_list[i].position = (300, 250 + offset)
        self.__is_display = False
        pass

    def update(self, delta_time: float):
        from pygame import mouse
        from gameobject import GRM
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER and (piece.state == State.IDLE or piece.state == State.READY_TO_MOVE) and piece.rect.collidepoint(mouse.get_pos()):
                self.display(piece)
                return
        self.__is_display = False
        self.__gun_info_list[1].string = str(GRM.shot_gun_range)
        self.__gun_info_list[3].string = str(max(GRM.shot_gun_damage-3, 1)) + "-" + str(GRM.shot_gun_damage)
        self.__gun_info_list[5].string = str(GRM.shot_gun_spray)
        for text in self.__gun_info_list:
            text.origin = (text.surface.get_rect().w/2, 0)

    def render(self):
        if self.__is_display:
            self.__health_lbl.render()
            self.__turn_lbl.render()
        else:
            for text in self.__gun_info_list:
                text.render()

    def display(self, piece):
        self.__is_display = True
        self.__health_lbl.string = f"Health: {piece.health}"
        self.__turn_lbl.string = f"Turn: {piece.turn_left}/{piece.queue_size}"
