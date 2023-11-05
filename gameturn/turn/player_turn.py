from gameturn.game_turn import Base
from enum import Enum


class MousePos(Enum):
    WANT_TO_MOVE = 0,
    WANT_TO_SHOOT = 1,
    OUT_OF_BOARD = 2,
    OUT_OF_WINDOW = 3


class PlayerTurn(Base):
    def __init__(self):
        super().__init__()
        self.__player_pos = None
        self.__move_list = []
        self.__player_intent = MousePos.OUT_OF_WINDOW
        self.__use_soul_card = False

    def init(self):
        from gameobject.chess import ChessBoard
        from utils import MoveGen
        for piece in ChessBoard.chess_list:
            piece.is_end_turn = True
        ChessBoard.player.gun.reset()
        self.isPerforming = False
        self.__use_soul_card = False
        self.__player_pos = ChessBoard.player.current_pos
        self.__move_list = MoveGen.get_king_move(self.__player_pos)

    def update(self, delta_time: float()):
        super().update(delta_time)
        from gameturn import GTM
        from gameturn.game_turn import Turn
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type
        if self.isPerforming is False:
            self.__handle_player_event()
        else:
            # check if the player's turn is finished
            if self.__is_end_player_turn():
                # if white king is dead, change to WIN_TURN
                if self.__handle_kill_piece():
                    GTM.change_turn(Turn.WIN)
                    return
                # if player makes a mistake
                if self.__handle_check_king():
                    GTM.change_turn(Turn.LOSE)
                    return

                is_bot_turn = False
                for piece in ChessBoard.chess_list:
                    if piece.type != Type.PLAYER:
                        piece.count_turn_left()
                        if piece.turn_left == 0:
                            is_bot_turn = True

                # reload gun ammo
                if self.__player_intent == MousePos.WANT_TO_MOVE or self.__use_soul_card:
                    if ChessBoard.player.gun.current_ammo < ChessBoard.player.gun.max_ammo and ChessBoard.player.gun.current_capacity > 0:
                        ChessBoard.player.gun.add_ammo()
                    else:
                        ChessBoard.player.gun.add_capacity()

                if is_bot_turn:
                    GTM.change_turn(Turn.BOT)
                else:
                    GTM.change_turn(Turn.PLAYER)
            else:
                # if player shoots:
                if self.__use_soul_card is False and self.__player_intent == MousePos.WANT_TO_SHOOT and ChessBoard.player.gun.finish_shoot is False:
                    self.__handle_bullet_hit_box()

        for piece in ChessBoard.chess_list:
            piece.update(delta_time)

    def render(self):
        from gameobject.chess import ChessBoard
        if len(ChessBoard.chess_list) == 1:
            ChessBoard.player.render()
            return
        k = len(ChessBoard.chess_list)
        for piece in ChessBoard.chess_list:
            if piece:
                piece.render()

    def __is_end_player_turn(self) -> bool:
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                if piece.is_end_turn is False:
                    return False
        if ChessBoard.player.is_end_turn and ChessBoard.player.state == State.IDLE:
            return True
        return False

    def __get_player_intention(self) -> MousePos:
        from gameobject.chess import ChessBoard
        for pos in self.__move_list:
            if ChessBoard.get_check_box(pos.x, pos.y).is_mouse_hover:
                return MousePos.WANT_TO_MOVE

        for y in range(8):
            for x in range(8):
                if ChessBoard.get_check_box(x, y).is_mouse_hover:
                    if self.__player_pos.x == x and self.__player_pos.y == y:
                        return MousePos.WANT_TO_MOVE
                    return MousePos.WANT_TO_SHOOT

        return MousePos.OUT_OF_BOARD

    def __hide_nearby_box(self):
        from gameobject.chess import ChessBoard
        for pos in self.__move_list:
            ChessBoard.get_check_box(pos.x, pos.y).hideOutline()

    def __handle_player_event(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import State
        # Using soul card
        if ChessBoard.player.state != State.IDLE:
            return
        if ChessBoard.player.gun.finish_shoot is False:
            return

        # if self.__use_soul_card:
        #     self.__handle_soul_card_event(ChessBoard.soul_card.piece)

        # if ChessBoard.soul_card.is_hover:
            #  if (sf::Mouse::isButtonPressed(sf::Mouse::Left) && ChessBoard->getSoulCard()->hasSoul()) {
            #             useSoulCard = true;
            #             return;
            #         }
            pass

        # other event
        ChessBoard.player.gun.set_shootable(False)
        self.__player_intent = self.__get_player_intention()
        if self.__player_intent == MousePos.WANT_TO_MOVE:
            self.__handle_move_event()
        elif self.__player_intent == MousePos.WANT_TO_SHOOT:
            self.__hide_nearby_box()
            self.__handle_shoot_event()
        elif self.__player_intent == MousePos.OUT_OF_BOARD:
            self.__hide_nearby_box()

    def __handle_move_event(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import State
        for pos in self.__move_list:
            if ChessBoard.get_check_box(pos.x, pos.y).is_mouse_hover:
                ChessBoard.get_check_box(pos.x, pos.y).showOutline()
                if ChessBoard.get_check_box(pos.x, pos.y).is_mouse_click:
                    ChessBoard.get_check_box(pos.x, pos.y).hideOutline()
                    ChessBoard.player.perform_turn()
                    ChessBoard.player.dest_pos = pos
                    ChessBoard.player.state = State.MOVING
                    self.isPerforming = True
                    return
            else:
                ChessBoard.get_check_box(pos.x, pos.y).hideOutline()

    def __handle_soul_card_event(self):
        pass

    def __handle_shoot_event(self):
        from gameobject.chess import ChessBoard
        from pygame import mouse
        ChessBoard.player.gun.set_shootable(True)
        if ChessBoard.player.gun.current_ammo == 0:
            return
        if mouse.get_pressed()[0]:
            ChessBoard.player.gun.shoot()
            ChessBoard.player.perform_turn()
            self.isPerforming = True

    def __handle_bullet_hit_box(self):
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        for bullet in ChessBoard.player.gun.bullets:
            for piece in ChessBoard.chess_list:
                if piece.type != Type.PLAYER and piece.rect.collidepoint(bullet.get_hitbox()) and bullet.is_flying:
                    bullet.stop()
                    if piece.state == State.HURT or piece.state == State.KILL or piece.state == State.DEAD:
                        continue
                    piece.shoot_pos = ChessBoard.player.current_pos
                    if bullet.get_damage() >= piece.health:
                        piece.state = State.KILL
                        if piece.type != Type.PAWN and piece.type != Type.KING:
                            # ChessBoard->getSoulCard()->setPiece(piece->getType());
                            pass
                    else:
                        piece.take_damage(bullet.get_damage())
                        piece.state = State.HURT

                    piece.perform_turn()

    def __handle_kill_piece(self) -> bool:
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        dead_count = 0
        is_white_king_dead = False
        i = 0
        while i < len(ChessBoard.chess_list):
            if ChessBoard.chess_list[i].state == State.DEAD:
                # CCounter->addAmount(GameRule->getPriceChess(ChessBoard->getChessList()[i]->getType()));
                if ChessBoard.chess_list[i].type == Type.KING:
                    is_white_king_dead = True
                ChessBoard.chess_list.pop(i)
                i -= 1
                dead_count += 1
            i += 1
        return is_white_king_dead

    def __handle_check_king(self) -> bool:
        from gameobject.chess import ChessBoard
        from gameobject.chess.chess_piece import Type, State
        from utils import MoveGen
        self.__player_pos = ChessBoard.player.current_pos
        for piece in ChessBoard.chess_list:
            if piece.type != Type.PLAYER:
                pos = MoveGen.get_next_move(piece)
                # if piece kill player
                if pos == self.__player_pos:
                    piece.turn_left = 0
                    piece.dest_pos = self.__player_pos
                    piece.state = State.MOVING
                    piece.perform_turn()
                    return True
        return False
        pass
