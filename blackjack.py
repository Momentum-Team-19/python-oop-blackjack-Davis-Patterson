import random
import os
from card_values import CARD_VALUES
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self,  rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def __str__(self):
        cards_str = ', '.join(str(card) for card in self.cards)
        return f'Deck of {len(self.cards)} cards: {cards_str}'

    def shuffle(self):
        shuffle_count = 100000
        for _ in range(shuffle_count):
            x = random.randint(0, len(self.cards)-1)
            y = random.randint(0, len(self.cards)-1)

            temp = self.cards[x]
            self.cards[x] = self.cards[y]
            self.cards[y] = temp


class Player:
    def __init__(self, name):
        self.name = input('What is your name? > ')
        self.hand = []

    def show_hand(self):
        print(f"{self.name} has: {', '.join(str(card) for card in self.hand)}")


class Dealer(Player):
    def __init__(self, name='Dealer'):
        self.name = 'Dealer'
        self.hand = []

    def __str__():
        return 'Dealer'


class Game:
    def __init__(self):
        self.name = 'Blackjack'
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player('miles')
        self.dealer = Dealer()

    def __str__(self):
        return self.name

    def deal_card(self, player):
        if self.deck.cards:
            card = self.deck.cards.pop(0)
            player.hand.append(card)
        else:
            print('No more cards')

    def play_hand(self):
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.player.show_hand()
        self.dealer.show_hand()
        
    def eval_hand(self):
        for card in self.player.hand:

    def play_game(self):
        print(f'Welcome to {self.name}!')
        print(self.deck)
        self.play_hand()



new_game = Game()
new_game.play_game()

# new_deck = Deck()
# print(new_deck)

# p1 = Player('Tim')
# p2 = Player('Bill')
# p3 = Dealer()
# p1.show_hand()
# p2.show_hand()
# p3.show_hand()
# new_deck.shuffle()
# print(new_deck)

# new_game.deal_card(new_deck, p1)
# new_game.deal_card(new_deck, p2)
# new_game.deal_card(new_deck, p3)
# p1.show_hand()
# p2.show_hand()
# p3.show_hand()

