from Model import Card


class GameState:
    def __init__(self, round_number, active_player_id, cards_on_board: Card, toep_called, player_lives, current_turn_order):
        self.current_turn_order = current_turn_order
        self.player_lives = player_lives
        self.toep_called = toep_called
        self.cards_on_board = cards_on_board
        self.active_player_id = active_player_id
        self.round_number = round_number
       