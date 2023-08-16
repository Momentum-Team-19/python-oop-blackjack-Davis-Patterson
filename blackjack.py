import random
import time
import os
from card_values import CARD_VALUES
import pyfiglet
import pygame
import colorama
from colorama import Fore

colorama.init(autoreset=True)

pygame.mixer.init()

current_directory = os.path.dirname(__file__)
music_path = os.path.join(current_directory, 'sfx', 'blackjack_loop.mp3')

SUITS = [
    f'{Fore.BLUE}♠{Fore.WHITE}', f'{Fore.RED}❤{Fore.WHITE}',
    f'{Fore.RED}♦{Fore.WHITE}', f'{Fore.BLUE}♣{Fore.WHITE}']
# SUITS = ['♠', '❤', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        self.used_cards = []

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
        self.total = 0
        self.score = 0

    def __str__(self):
        return self.name

    def show_hand(self):
        print(f"{self.name} has: {', '.join(str(card) for card in self.hand)}")


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.total = 0
        self.score = 0

    def __str__(self):
        return self.name


class Game:
    def __init__(self):
        self.name = 'Blackjack'
        self.deck = Deck()
        # self.deck.shuffle()
        self.player = Player(input('What is your name? > '))
        self.dealer = Dealer()

    def __str__(self):
        return self.name

    def clear_cards(self):
        self.deck.used_cards.extend(self.player.hand)
        self.deck.used_cards.extend(self.dealer.hand)
        self.player.hand.clear()
        self.dealer.hand.clear()

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

    def calc_hand(self, player):
        total = 0

        for card in player.hand:
            rank = card.rank
            if rank in CARD_VALUES:
                total += CARD_VALUES[rank]
                if rank == 'A' and total >= 22:
                    total -= 10

        return total

    def hit_me(self):
        while self.player.total < 21:
            hit_me = input(
                'Do you want another card? (y/n) > ').lower().strip()
            if hit_me == 'n':
                break

            elif hit_me == 'y':
                    self.deal_card(self.player)
                    self.player.show_hand()
                    self.player.total = self.calc_hand(self.player)
                    print(f"{self.player.name}'s total: {self.player.total}")

            else:
                ("Please enter either 'y' or 'n'")

        else: print(f"{self.player.name}'s total: {self.player.total}")

        return self.player.total

    def dealer_hit(self):
        while self.dealer.total < 16:
            self.deal_card(self.dealer)
            self.dealer.show_hand()
            self.dealer.total = self.calc_hand(self.dealer)
            print(f"{self.dealer.name}'s total: {self.dealer.total}")
            if self.dealer.total >= 16:
                break
        return self.dealer.total

    def eval_hands(self):
        player_total = self.calc_hand(self.player)
        dealer_total = self.calc_hand(self.dealer)

        if player_total > 21:
            return "Dealer"
        elif dealer_total > 21:
            return self.player.name
        elif player_total > dealer_total:
            return self.player.name
        elif dealer_total > player_total:
            return "Dealer"
        else:
            return "Draw"

    def play_game(self):
        play_flag = True
        welcome_text = pyfiglet.figlet_format(text='Welcome to', font='small')
        print(welcome_text)
        game_name_text = pyfiglet.figlet_format(
            text=f'{self.name}', font='big')
        print(game_name_text)
        player_name_text = pyfiglet.figlet_format(
            text=f'{self.player.name}!', font='smslant')
        print(player_name_text)
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
        while play_flag:
            print(self.deck)
            self.play_hand()
            player_total = self.calc_hand(self.player)
            dealer_total = self.calc_hand(self.dealer)
            print(f"{self.player.name}'s total: {player_total}")
            print(f"{self.dealer.name}'s total: {dealer_total}")
            if player_total < 21:
                player_total = self.hit_me()
            dealer_total = self.dealer_hit()

            time.sleep(.2)
            print('...')
            self.player.show_hand()
            print(f"{self.player.name}'s final total: {player_total}")
            self.dealer.show_hand()
            print(f"{self.dealer.name}'s final total: {dealer_total}")
            winner = self.eval_hands()
            if winner == f'{self.player.name}':
                self.player.score += 1
                print(f'Winner: {winner}!')
            if winner == 'Dealer':
                self.dealer.score += 1
                print(f'Winner: {winner}!')
            if winner == 'Draw':
                print(
                    f'Draw!\nEach player had a total of {player_total}\n')
                print('There is no winner')
            time.sleep(.5)
            print('...')

            while True:
                play_again = input(
                    'Do you want to play again? (y/n) > ').lower().strip()
                if play_again == 'n':
                    play_flag = False
                    break
                elif play_again == 'y':
                    print('Resetting game')
                    self.clear_cards()
                    player_total = 0
                    dealer_total = 0
                    break

                else:
                    print("Please enter 'y' or 'n'")


new_game = Game()
new_game.play_game()
