from enum import Enum, auto


class StateTypes(Enum):
    INVALID = 0
    INTRO = auto()
    MENU = auto()
    ABOUT = auto()
    PLAY = auto()
    MODE_SELECT = auto()
    UPGRADE = auto()
    END = auto()
