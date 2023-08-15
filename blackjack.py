import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit} {self.rank}'


class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
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
        super().__init__(name)  # super means 'parent', calls whatever is in the parent, if nothing is different then don't write it (it'll default to parent init)

    def __str__():
        return 'Dealer'


class Game:
    def __init__(self):
        self.name = 'Blackjack'
        self.player_count = 0
        self.players = []
        self.deck = Deck()

    def __str__(self):
        return self.name
    
    def add_players(self, player):
        self.players.append(player)
        self.player_count += 1

    def deal_card(self, player):
        if self.deck.cards:
            card = self.deck.cards.pop(0)
            player.hand.append(card)
        else:
            print('No more cards')

    def play_hand(self):
        for _ in range(2):
            for player in self.players:
                self.deal_card(self.deck, player)

    def play_game(self):
        print(f'Welcome to {self.name}!')
        player_name = input('What is your name? > ')
        self.add_players(f'{player_name}')
        self.add_players(Dealer())
        print(self.players)
        print(self.player_count)
        self.deck.shuffle()
        print(self.deck)
        # self.play_hand()



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

