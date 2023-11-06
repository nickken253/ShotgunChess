from gamemanager import WConnect, DATA
from gamestate.game_state_base import GameStateBase
from gamestate import GSM


class GSUpgrade(GameStateBase):
    def __init__(self):
        super().__init__()
        self.background = None
        from gameobject.text import Text
        self.title = Text()
        self.btn_continue = None
        from gameobject.sprite import Sprite
        self.shop_board = Sprite()
        self.shop_btn_list = []
        self.current_time = 0.0

    def __del__(self):
        pass

    def exit(self):
        super().exit()

    def pause(self):
        super().pause()

    def resume(self):
        super().resume()

    def init(self):
        super().init()
        import game_config
        self.background = DATA.get_texture("bg2")

        from gameobject.game_button import GameButton
        self.btn_continue = GameButton("btnContinue", (172.0, 62.0))
        self.btn_continue.init()
        self.btn_continue.position = (985.0, 520.0)
        self.btn_continue.set_on_click(lambda: (
            GSM.pop_state(),
            # ChessBoard.setLevel(GameRule.getCurrentLevel() + 1);
        ))

        font = DATA.get_font("Silver_62")
        # font.set_bold(True)
        self.title.string = "Merchant's Shop"
        self.title.set_font(font)
        self.title.position = (390.0, 25.0)

        self.shop_board.texture = DATA.get_texture("\\gui\\shopBoard")
        self.shop_board.origin = (842.0 / 2, 0.0)
        self.shop_board.position = (game_config.SCREEN_WIDTH / 2, 185.0)

        for i in range(5):
            from gameobject.shop_button import ShopButton
            shop_btn = ShopButton()
            self.shop_btn_list.append(shop_btn)
        self.shop_btn_list[0].init("RANGE", 700)
        # self.shop_btn_list[0].set_value()
        # self.shop_btn_list[0].set_on_click()

        self.shop_btn_list[1].init("DAMAGE", 1200)
        # self.shop_btn_list[1].set_value()
        # self.shop_btn_list[1].set_on_click()

        self.shop_btn_list[2].init("PELLETS", 1800)
        # self.shop_btn_list[2].set_value()
        # self.shop_btn_list[2].set_on_click()

        self.shop_btn_list[3].init("MAX AMMO", 2000)
        # self.shop_btn_list[3].set_value()
        # self.shop_btn_list[3].set_on_click()

        self.shop_btn_list[4].init("MAX CAPACITY", 1500)
        # self.shop_btn_list[4].set_value()
        # self.shop_btn_list[4].set_on_click()

        for i in range(5):
            self.shop_btn_list[i].set_position((482.0, 221.0 + 47.0 * i))

    def update(self, delta_time: float):
        super().update(delta_time)
        import game_config
        self.current_time += delta_time
        if self.current_time < game_config.TRANSITION_DURATION * 2:
            pass
        else:
            self.handle_upgrade(delta_time)
            return
        self.update_color()

    def render(self):
        super().render()
        WConnect.get_window().blit(self.background, (0, 0))
        self.btn_continue.render()
        WConnect.get_window().blit(self.shop_board.texture, self.shop_board.absolute_position)
        self.title.render()
        for btn in self.shop_btn_list:
            btn.render()

    def update_color(self):
        pass

    def handle_upgrade(self, delta_time: float):
        self.btn_continue.update(delta_time)
        for btn in self.shop_btn_list:
            btn.update(delta_time)
        # CCounter.update(delta_time)
