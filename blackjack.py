import random
import os
from card_values import CARD_VALUES
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

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
        self.name = name
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
        # self.deck.shuffle()
        self.player = Player(input('What is your name? > '))
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

    def eval_hand(self, player):
        total = 0

        for card in player.hand:
            rank = card.rank
            if rank in CARD_VALUES:
                total += CARD_VALUES[rank]
                if rank == 'A' and total >= 22:
                    total -= 10

        return total

    def hit_me(self, player_total):
        while player_total < 21:
            hit_me = input('Do you want another card? (y/n) > ').lower().strip()
            if hit_me == 'n':
                print(f'No card given to {self.player}')
                return player_total

            if player_total > 21:
                return player_total

            elif hit_me == 'y':
                self.deal_card(self.player)
                self.player.show_hand()
                player_total = self.eval_hand(self.player)
                print(f"{self.player.name}'s total: {player_total}")
                return player_total
            
            else:
                ("Please enter either 'y' or 'n'")

    def play_game(self):
        print(f'Welcome to {self.name}!')
        print(self.deck)
        self.play_hand()
        player_total = self.eval_hand(self.player)
        dealer_total = self.eval_hand(self.dealer)
        print(f"{self.player.name}'s total: {player_total}")
        print(f"{self.dealer.name}'s total: {dealer_total}")
        player_total = self.hit_me(player_total)
        print(f"{self.player.name}'s total: {player_total}")
        while dealer_total <= 16:
            self.deal_card(self.dealer)
            dealer_total = self.eval_hand(self.dealer)
            print(f"{self.dealer.name}'s total: {dealer_total}")



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

