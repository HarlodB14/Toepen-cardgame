from Card import Card


class Player:
    def __init__(self, player_id, name, card: Card):
        self.player_id = player_id
        self.card = card
        self.name = name
