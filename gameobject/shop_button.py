import pygame.mouse

from gamemanager import DATA
from gameobject.rectangle import Rectangle
from gameobject.text import Text


class ShopButton:
    def __init__(self):
        self.current_time = 0.0
        self.is_handling = False
        self.is_hover = False
        self.payable = False
        self.name = None
        self.btn_get_value = None
        self.lbl_title = Text()
        self.lbl_price = Text()
        self.selected = None
        self.price = 0
        self.btn_click_func = None

    def __del__(self):
        pass

    def init(self, name: str, price: int):
        self.name = name
        # self.selected = Rectangle((0, 0), (540.0, 47.0))
        # self.selected.border_color = (255, 255, 255)
        #
        # font_title = DATA.get_font("Silver_50")
        # # font_title.bold = True
        # self.lbl_title.string = self.name
        # self.lbl_title.color = (56, 52, 80)
        # self.lbl_title.set_font(font_title)
        #
        # font_price = DATA.get_font("Silver_38")
        # # font_price.bold = True
        # self.lbl_price.string = "upgrade cost: " + str(price)
        # self.lbl_price.color = (56, 52, 80)
        # self.lbl_price.set_font(font_price)

    def update(self, delta_time: float):
        new_title = self.name
        # new_title = self.name+": "+str(self.btn_get_value())
        self.lbl_title.string = new_title

        # CCounter
        # if CCounter->getCurrentCash() < self.price:
        #     self.payable = False
        # else:
        #     self.payable = True

        if self.is_handling:
            self.current_time += delta_time
            if self.current_time > 0.25:
                self.current_time = 0.0
                self.is_handling = False
            else:
                return

        if self.selected.contain(pygame.mouse.get_pos()):
            self.is_hover = True
            if pygame.mouse.get_pressed()[0]:
                self.is_handling = True
                if self.payable:
                    # CCounter.add_amount(-self.price)
                    DATA.play_sound("cash")
                    self.btn_click_func()
        else:
            self.is_hover = False

    def render(self):
        if self.is_hover and self.payable:
            self.selected.render()
            self.lbl_price.render()
        self.lbl_title.render()

    def set_value(self, func):
        self.btn_get_value = func

    def set_position(self, position):
        self.selected.position = position
        self.lbl_title.position = (position[0] + 12.0, position[1] + 3.0)
        x = position[0] + self.selected.rect.size[0] - self.lbl_price.surface.get_size()[0] - 12.0
        self.lbl_price.position = (x, position[1] + 6.0)

    def set_on_click(self, func):
        self.btn_click_func = func
