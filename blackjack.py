import random


class Deck:
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return f'{self.rank}{self.suit}'

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                new_card = self.Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        cards_str = ', '.join(str(card) for card in self.cards)
        return f'Deck of {len(self.cards)} cards: {cards_str}'

    def shuffle(self):
        random.shuffle(self.cards)


new_deck = Deck()
print(new_deck)
