from gamemanager import WConnect, DATA
from gamestate.game_state_base import GameStateBase
from gamestate import GSM


class GSUpgrade(GameStateBase):
    def __init__(self):
        super().__init__()
        from gameobject.sprite import Sprite
        self.background = Sprite()
        from gameobject.text import Text
        self.title = Text()
        self.btn_continue = None
        self.shop_board = Sprite()
        self.shop_btn_list = []
        self.current_time = 0.0
        self.alpha = 0

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
        from gameobject import GRM
        from gameobject.chess import CCounter
        self.background.texture = DATA.get_texture("bg2")

        from gameobject.game_button import GameButton
        self.btn_continue = GameButton("btnContinue", (172.0, 62.0))
        self.btn_continue.init()
        self.btn_continue.position = (985.0, 520.0)
        self.btn_continue.set_on_click(self.__btn_continue_on_click)

        font = DATA.get_font("Silver", 62)
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
        self.shop_btn_list[0].set_value(lambda: GRM.shot_gun_range)
        self.shop_btn_list[0].set_on_click(lambda: setattr(GRM, 'shot_gun_range', GRM.shot_gun_range + 50))

        self.shop_btn_list[1].init("DAMAGE", 1200)
        self.shop_btn_list[1].set_value(lambda: GRM.shot_gun_damage)
        self.shop_btn_list[1].set_on_click(lambda: setattr(GRM, 'shot_gun_damage', GRM.shot_gun_damage + 1))

        self.shop_btn_list[2].init("PELLETS", 1800)
        self.shop_btn_list[2].set_value(lambda: GRM.shot_gun_spray)
        self.shop_btn_list[2].set_on_click(lambda: setattr(GRM, 'shot_gun_spray', GRM.shot_gun_spray + 1))

        self.shop_btn_list[3].init("MAX AMMO", 2000)
        self.shop_btn_list[3].set_value(lambda: GRM.shot_gun_max_ammo)
        self.shop_btn_list[3].set_on_click(lambda: setattr(GRM, 'shot_gun_max_ammo', GRM.shot_gun_max_ammo + 1))

        self.shop_btn_list[4].init("MAX CAPACITY", 1500)
        self.shop_btn_list[4].set_value(lambda: GRM.shot_gun_max_capacity)
        self.shop_btn_list[4].set_on_click(lambda: setattr(GRM, 'shot_gun_max_capacity', GRM.shot_gun_max_capacity + 1))

        for i in range(5):
            self.shop_btn_list[i].set_position((482.0, 221.0 + 47.0 * i))

        # CCounter.init()
        self.alpha = 0
        self.update_color()

    def update(self, delta_time: float):
        super().update(delta_time)
        from game_config import TRANSITION_DURATION
        self.current_time += delta_time
        if self.current_time < TRANSITION_DURATION * 2:
            self.alpha = min(255, int(round(255*self.current_time/(TRANSITION_DURATION*2))))
        else:
            self.alpha = 255
            self.handle_upgrade(delta_time)
            return
        self.update_color()

    def render(self):
        super().render()
        WConnect.window.blit(self.background.texture, (0, 0))
        self.btn_continue.render()
        WConnect.window.blit(self.shop_board.texture, self.shop_board.absolute_position)
        self.title.render()
        for btn in self.shop_btn_list:
            btn.render()
        from gameobject.chess import CCounter
        CCounter.render()

    def update_color(self):
        self.background.alpha = self.alpha
        self.btn_continue.alpha = self.alpha
        self.shop_board.alpha = self.alpha

    def handle_upgrade(self, delta_time: float):
        self.btn_continue.update(delta_time)
        for btn in self.shop_btn_list:
            btn.update(delta_time)
        from gameobject.chess import CCounter
        CCounter.update(delta_time)

    def __btn_continue_on_click(self):
        GSM.pop_state()
        from gameobject.chess import ChessBoard
        from gameobject import GRM
        ChessBoard.set_level(GRM.current_level + 1)
