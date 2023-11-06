from gamemanager.singleton import Singleton


class CashCounter(metaclass=Singleton):
    def __init__(self):
        self.__lbl_cash = None
        self.__box_cash = None
        self.__current_cash = 0
        self.__new_cash = 0
        self.__amount_per_time = 0

    def init(self):
        from gamemanager import DATA
        from gameobject.sprite import Sprite
        from gameobject.text import Text
        self.__box_cash = Sprite()
        self.__box_cash.texture = DATA.get_texture("\\chess\\CashCounter")
        self.__box_cash.scale = (3, 3)
        self.__box_cash.position = (722, 28)

        self.__lbl_cash = Text()
        self.__lbl_cash.set_font(DATA.get_font("Silver", 36))
        self.__lbl_cash.position = (890, 36)
        self.__lbl_cash.color = (56, 82, 80)
        self.__update_text()

    def update(self, delta_time: float):
        if self.__current_cash != self.__new_cash:
            if abs(self.__amount_per_time) > abs(self.__new_cash - self.__current_cash):
                self.__amount_per_time = self.__new_cash - self.__current_cash
            self.__current_cash += self.__amount_per_time
            self.__update_text()

    def render(self):
        from gamemanager import WConnect
        WConnect.window.blit(self.__box_cash.texture, self.__box_cash.absolute_position)
        self.__lbl_cash.render()

    def add_amount(self, amount: int):
        self.__new_cash += amount
        if self.__new_cash > 999999999:
            self.__new_cash = 999999999
        if self.__new_cash < 0:
            self.__new_cash = 0
        self.__amount_per_time = (self.__new_cash - self.__current_cash) / 32
        if self.__amount_per_time == 0:
            if self.__new_cash > self.__current_cash:
                self.__amount_per_time = 1
            elif self.__new_cash < self.__current_cash:
                self.__amount_per_time = -1

    @property
    def current_cash(self) -> int:
        return self.__current_cash

    def reset(self):
        self.__current_cash = 0
        self.__new_cash = 0
        self.__amount_per_time = 0
        self.__update_text()

    def __update_text(self):
        self.__lbl_cash.string = str(int(self.__current_cash))
        self.__lbl_cash.origin = (self.__lbl_cash.surface.get_rect().w, 0)

