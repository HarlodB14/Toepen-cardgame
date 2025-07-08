class Card:
    SUITS = {
        "Hearts": {"symbol": "♥", "color": "RED", "name": "HEARTS"},
        "Diamonds": {"symbol": "♦", "color": "RED", "name": "DIAMONDS"},
        "Clubs": {"symbol": "♣", "color": "BLACK", "name": "CLUBS"},
        "Spades": {"symbol": "♠", "color": "BLACK", "name": "SPADES"},
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.value = rank
        self.symbol = self.SUITS[suit]["symbol"]
        self.color = self.SUITS[suit]["color"]
        self.name = f"{rank} of {suit}"

    def __str__(self):
        return f"{self.symbol}{self.value} ({self.color})"

    def getsuits(self):
        return self.SUITS
