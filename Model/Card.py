class Card:
    SUITS = {
        "Hearts": {"symbol": "♥", "color": "red", "name": "Hearts"},
        "Diamonds": {"symbol": "♦", "color": "red", "name": "Diamonds"},
        "Clubs": {"symbol": "♣", "color": "black", "name": "Clubs"},
        "Spades": {"symbol": "♠", "color": "black", "name": "Spades"},
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
