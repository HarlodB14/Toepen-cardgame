from Model.Card import Card


class Deck:
    def __init__(self):
        self.cards = self.generatedeck()

    def generatedeck(self):
        suits = Card.SUITS.keys()
        ranks = ["ACE", "KING", "QUEEN", "JACK", 10, 9, 8, 7, 6, 5, 4, 3, 2]
        deck = []

        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit,rank))
        return deck

    def printDeck(self):
        return "\n".join(str(card) for card in self.cards)

