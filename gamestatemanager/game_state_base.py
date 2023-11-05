from abc import ABC, abstractmethod

from gamestatemanager.state_types import StateTypes


class GameStateBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def update(self, delta_time: float):
        pass

    @abstractmethod
    def render(self):
        pass

    @staticmethod
    def create_state(state_type: StateTypes):
        from gamestatemanager.State.GSAbout import GSAbout
        from gamestatemanager.State.GSEnd import GSEnd
        from gamestatemanager.State.GSIntro import GSIntro
        from gamestatemanager.State.GSMenu import GSMenu
        from gamestatemanager.State.GSModeSelect import GSModeSelect
        from gamestatemanager.State.GSPlay import GSPlay
        from gamestatemanager.State.GSUpgrade import GSUpgrade
        game_state = None
        if state_type == StateTypes.INVALID:
            pass
        elif state_type == StateTypes.INTRO:
            game_state = GSIntro()
        elif state_type == StateTypes.MENU:
            game_state = GSMenu()
        elif state_type == StateTypes.ABOUT:
            game_state = GSAbout()
        elif state_type == StateTypes.PLAY:
            game_state = GSPlay()
        elif state_type == StateTypes.MODE_SELECT:
            game_state = GSModeSelect()
        elif state_type == StateTypes.UPGRADE:
            game_state = GSUpgrade()
        elif state_type == StateTypes.END:
            game_state = GSEnd()
        return game_state
