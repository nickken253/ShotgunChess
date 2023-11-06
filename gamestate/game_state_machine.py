from gamemanager.singleton import Singleton
from gamestate.game_state_base import GameStateBase
from gamestate.state_types import StateTypes


class GameStateMachine(metaclass=Singleton):
    def __init__(self):
        self.state_stack = []
        self.active_state = None
        self.next_state = None

    def __del__(self):
        while self.state_stack:
            self.state_stack.pop()
        self.state_stack.clear()

    def change_state(self, state_type: StateTypes):
        self.next_state = GameStateBase.create_state(state_type)

    def push_state(self, state_type: StateTypes):
        game_state = GameStateBase.create_state(state_type)
        if self.state_stack:
            self.state_stack[-1].pause()
        self.state_stack.append(game_state)

    def pop_state(self):
        if self.state_stack:
            self.state_stack[-1].exit()
            self.state_stack.pop()
        if self.state_stack:
            self.state_stack[-1].resume()
        self.active_state = self.state_stack[-1]

    def perform_state_change(self):
        if self.next_state is not None:
            if self.state_stack:
                self.state_stack[-1].exit()
            self.state_stack.append(self.next_state)
            self.state_stack[-1].init()
            self.active_state = self.next_state
            self.next_state = None
            pass

    def need_to_change_state(self) -> bool:
        return self.next_state is not None

    def has_state(self) -> bool:
        return len(self.state_stack) > 0
