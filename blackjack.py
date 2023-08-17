import random
import time
import os
from card_values import CARD_VALUES
from card_imgs import card_imgs
from textures import cards_txt, texture1
import pyfiglet
import pygame
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

pygame.mixer.init()
pygame.mixer.music.set_volume(.1)

current_directory = os.path.dirname(__file__)
music_path = os.path.join(current_directory, 'sfx', 'blackjack_loop.mp3')

# SUITS = [
#     f'{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}',
#     f'{Fore.RED}❤{Fore.WHITE}',
#     f'{Fore.RED}♦{Fore.WHITE}',
#     f'{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}'
# ]
SUITS = ['♠', '❤', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_FORMATS = {
    '♠': f'{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}',
    '❤': f'{Fore.RED}❤{Fore.WHITE}',
    '♦': f'{Fore.RED}♦{Fore.WHITE}',
    '♣': f'{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}'
}

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
        print(f"{self.name} has: ")
        for line in range(7):
            hand_line = '  '.join([card_imgs[str(card)][line] for card in self.hand])
            print(hand_line)
        print()

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
        if not self.deck.cards:
            print('Reshuffling the deck')  # <= RESHUFFLES DECK WHEN EMPTY
            time.sleep(.5)
            print('...')
            time.sleep(.5)
            self.deck.cards.extend(self.deck.used_cards)
            self.deck.used_cards = []
            self.deck.shuffle()

        card = self.deck.cards.pop(0)
        player.hand.append(card)

    def play_hand(self):
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.dealer.total = self.calc_hand(self.dealer)
        self.player.total = self.calc_hand(self.player)

        self.dealer.show_hand()
        self.dealer.total = self.calc_hand(self.dealer)
        self.player.total = self.calc_hand(self.player)
        if self.dealer.total >= 22:
            dealer_total_color = Fore.RED
        elif self.player.total > 21 and self.dealer.total <= 21:
            dealer_total_color = Fore.GREEN
        elif self.dealer.total > self.player.total and self.dealer.total <= 21:
            dealer_total_color = Fore.GREEN
        elif self.dealer.total < self.player.total and self.player.total <= 21:
            dealer_total_color = Fore.RED
        else:
            dealer_total_color = Fore.RED
        print(f"{self.dealer.name}'s total: {dealer_total_color}{self.dealer.total}{Fore.WHITE}\n")

        self.player.show_hand()
        if self.player.total >= 22:
            player_total_color = Fore.RED
        if self.dealer.total > 21 and self.player.total <= 21:
            player_total_color = Fore.GREEN
        elif self.player.total > self.dealer.total and self.player.total <= 21:
            player_total_color = Fore.GREEN
        elif self.player.total < self.dealer.total and self.dealer.total <= 21:
            player_total_color = Fore.RED
        else:
            player_total_color = Fore.RED
        print(f"{self.player.name}'s total: {player_total_color}{self.player.total}{Fore.WHITE}\n")


    def calc_hand(self, player):
        total = 0
        has_ace = False

        for card in player.hand:
            rank = card.rank.upper()
            if rank in CARD_VALUES:
                total += CARD_VALUES[rank]
                if rank == 'A':
                    has_ace = True
        
        if has_ace and total >= 22:
            total -= 10

        return total

    def hit_me(self):
        while self.player.total < 21:
            if not self.deck.cards:
                print('No more cards\n')
                break
            
            hit_me = input(
                'Do you want another card? (y/n) > ').lower().strip()
            if hit_me == 'n':
                print('\n')
                break

            elif hit_me == 'y':
                self.deal_card(self.player)
                os.system('clear')

                self.dealer.show_hand()
                self.dealer.total = self.calc_hand(self.dealer)
                self.player.total = self.calc_hand(self.player)
                if self.dealer.total >= 22:
                    dealer_total_color = Fore.RED
                elif self.player.total > 21 and self.dealer.total <= 21:
                    dealer_total_color = Fore.GREEN
                elif self.dealer.total > self.player.total and self.dealer.total <= 21:
                    dealer_total_color = Fore.GREEN
                elif self.dealer.total < self.player.total and self.player.total <= 21:
                    dealer_total_color = Fore.RED
                else:
                    dealer_total_color = Fore.RED
                print(f"{self.dealer.name}'s total: {dealer_total_color}{self.dealer.total}{Fore.WHITE}\n")

                self.player.show_hand()
                if self.player.total >= 22:
                    player_total_color = Fore.RED
                if self.dealer.total > 21 and self.player.total <= 21:
                    player_total_color = Fore.GREEN
                elif self.player.total > self.dealer.total and self.player.total <= 21:
                    player_total_color = Fore.GREEN
                elif self.player.total < self.dealer.total and self.dealer.total <= 21:
                    player_total_color = Fore.RED
                else:
                    player_total_color = Fore.RED
                print(f"{self.player.name}'s total: {player_total_color}{self.player.total}{Fore.WHITE}\n")

            else:
                invalid_text = pyfiglet.figlet_format(
                    text='IVALID', font='small')
                print(f'{Fore.RED}{invalid_text}')
                print("Please enter either 'y' or 'n'\n")

        return self.player.total

    def dealer_hit(self):
        while self.dealer.total < 16:
            if not self.deck.cards:
                print("No more cards")
                break
            self.deal_card(self.dealer)
            os.system('clear')
            
            self.dealer.show_hand()
            self.dealer.total = self.calc_hand(self.dealer)
            self.player.total = self.calc_hand(self.player)
            if self.dealer.total >= 22:
                dealer_total_color = Fore.RED
            elif self.player.total > 21 and self.dealer.total <= 21:
                dealer_total_color = Fore.GREEN
            elif self.dealer.total > self.player.total and self.dealer.total <= 21:
                dealer_total_color = Fore.GREEN
            elif self.dealer.total < self.player.total and self.player.total <= 21:
                dealer_total_color = Fore.RED
            else:
                dealer_total_color = Fore.RED
            print(f"{self.dealer.name}'s total: {dealer_total_color}{self.dealer.total}{Fore.WHITE}\n")

            self.player.show_hand()
            if self.player.total >= 22:
                player_total_color = Fore.RED
            if self.dealer.total > 21 and self.player.total <= 21:
                player_total_color = Fore.GREEN
            elif self.player.total > self.dealer.total and self.player.total <= 21:
                player_total_color = Fore.GREEN
            elif self.player.total < self.dealer.total and self.dealer.total <= 21:
                player_total_color = Fore.RED
            else:
                player_total_color = Fore.RED
            print(f"{self.player.name}'s total: {player_total_color}{self.player.total}{Fore.WHITE}\n")

            print('...')
            time.sleep(1)
            if self.dealer.total >= 16:
                break
        return self.dealer.total

    def eval_hands(self):
        self.player.total = self.calc_hand(self.player)
        self.dealer.total = self.calc_hand(self.dealer)

        if self.player.total > 21:
            return "Dealer"
        elif self.dealer.total > 21:
            return self.player.name
        elif self.player.total > self.dealer.total:
            return self.player.name
        elif self.dealer.total > self.player.total:
            return "Dealer"
        else:
            return "Draw"

    def play_game(self):
        play_flag = True
        while play_flag:
            self.player.total = 0
            self.dealer.total = 0
            os.system('clear')

            # print(self.deck)  # <= PRINTS THE WHOLE DECK AT START OF PLAY

            self.play_hand()
            
            if self.player.total < 21:
                self.player.total = self.hit_me()
            if self.player.total <= 21 and self.dealer.total <= 16:
                self.dealer.total = self.dealer_hit()

            os.system('clear')

            self.dealer.show_hand()
            self.dealer.total = self.calc_hand(self.dealer)
            self.player.total = self.calc_hand(self.player)
            if self.dealer.total >= 22:
                dealer_total_color = Fore.RED
            elif self.player.total > 21 and self.dealer.total <= 21:
                dealer_total_color = Fore.GREEN
            elif self.dealer.total > self.player.total and self.dealer.total <= 21:
                dealer_total_color = Fore.GREEN
            elif self.dealer.total < self.player.total and self.player.total <= 21:
                dealer_total_color = Fore.RED
            else:
                dealer_total_color = Fore.RED
            print(f"{self.dealer.name}'s final total: {dealer_total_color}{self.dealer.total}{Fore.WHITE}\n")

            self.player.show_hand()
            if self.player.total >= 22:
                player_total_color = Fore.RED
            if self.dealer.total > 21 and self.player.total <= 21:
                player_total_color = Fore.GREEN
            elif self.player.total > self.dealer.total and self.player.total <= 21:
                player_total_color = Fore.GREEN
            elif self.player.total < self.dealer.total and self.dealer.total <= 21:
                player_total_color = Fore.RED
            else:
                player_total_color = Fore.RED
            print(f"{self.player.name}'s final total: {player_total_color}{self.player.total}{Fore.WHITE}\n")
            
            winner = self.eval_hands()
            if winner == f'{self.player.name}':
                self.player.score += 1
                print(f'Winner: {winner}!\nWith a score of {Fore.GREEN}{self.player.total}{Fore.WHITE}\n')
            if winner == 'Dealer':
                self.dealer.score += 1
                print(f'Winner: {winner} :(\nWith a score of {Fore.RED}{self.dealer.total}{Fore.WHITE}\n')
            if winner == 'Draw':
                print(
                    f'Draw!\nEach player had a total of {Fore.RED}{self.player.total}{Fore.WHITE}')
                print('There is no winner\n')
            time.sleep(.5)
            print('...\n')

            while True:
                play_again = input(
                    'Do you want to play again? (y/n) > ').lower().strip()
                if play_again == 'n':
                    time.sleep(.5)
                    print('\n...\n')
                    time.sleep(.5)
                    play_flag = False
                    break
                elif play_again == 'y':
                    resetting_game = pyfiglet.figlet_format(text='Resetting', font='smslant')
                    print(f'\n{resetting_game}')
                    time.sleep(.5)
                    self.clear_cards()
                    self.player.total = 0
                    self.dealer.total = 0
                    break

                else:
                    invalid_text = pyfiglet.figlet_format(
                    text='IVALID', font='small')
                    print(f'{Fore.RED}{invalid_text}')
                    print("Please enter 'y' or 'n'")
                    invalid_text = pyfiglet.figlet_format(
                        text='IVALID', font='small')
                    print(f'{Fore.RED}{invalid_text}')


class Menu:
    def __init__(self):
        os.system('clear')
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
        time.sleep(.5)
        welcome_text = pyfiglet.figlet_format(text='Welcome to', font='small')
        print(f'\n{welcome_text}')
        time.sleep(.5)
        game_name_text = pyfiglet.figlet_format(
            text='Blackjack', font='big')
        print(game_name_text)
        time.sleep(1)
        menu_flag = True
        while menu_flag:
            self.print_texture(cards_txt)
            print('\n')
            self.print_texture(texture1)
            menu_text = pyfiglet.figlet_format(text="Menu", font="rectangles")
            print(menu_text)
            print('Options:\n[P]lay game\n[V]iew scores\n[S]ettings\n[E]xit\n')
            menu_choice = input('Please select an option > ').lower().strip()
            if menu_choice == 'p':
                new_game = Game()
                new_game.play_game()
                

            if menu_choice == 'v':
                print(f"The Player's score is: {new_game.player.score}")
                print(f"The Dealer's score is: {new_game.dealer.score}")

            elif menu_choice == 's':
                time.sleep(.5)
                print('...')
                settings_text = pyfiglet.figlet_format(
                    text="Settings", font="small")
                print(settings_text)
                print('Options:\n[V]olume settings\n[R]ender cards\n[E]xit\n')
                while True:
                    settings_choice = input(
                        'Please select an option > ').lower().strip()
                    if settings_choice == 'v':
                        while True:
                            volume_input = input("Enter volume value (0.0 - 1.0) > ")

                            try:
                                volume = float(volume_input)
                                if 0.0 <= volume <= 1.0:
                                    pygame.mixer.music.set_volume(volume)
                                    print('...')
                                    print(f"Volume set to {Fore.GREEN}{volume}{Fore.WHITE}")
                                    print('...')
                                    time.sleep(.5)
                                    break
                                else:
                                    print('...')
                                    invalid_text = pyfiglet.figlet_format(text='IVALID', font='small')
                                    print(f'{Fore.RED}{invalid_text}')
                                    print("Please enter a value between 0.0 and 1.0.")
                                    print('...')
                                    time.sleep(.5)
                            except ValueError:
                                print('...')
                                invalid_text = pyfiglet.figlet_format(text='IVALID', font='small')
                                print(f'{Fore.RED}{invalid_text}')
                                print(f"{Fore.RED}'VALUE ERROR'{Fore.WHITE}")
                                print('...')
                        break

                    if settings_choice == 'r':
                        print('...')
                        time.sleep(.5)
                        self.view_all_cards()

                    if settings_choice == 'e':
                        break

                    else:
                        invalid_text = pyfiglet.figlet_format(text='IVALID', font='small')
                        print(f'{Fore.RED}{invalid_text}')
                        print('Please enter a valid option.')

            elif menu_choice == 'e':
                exit()

            else:
                invalid_text = pyfiglet.figlet_format(
                    text='IVALID', font='small')
                print(f'{Fore.CYAN}{invalid_text}')
                print('Please enter a valid option')

    def __str__(self):
        return 'Menu'
    
    def view_all_cards(self):
        print(f'Deck has {Fore.GREEN}{len(card_imgs)}{Fore.WHITE} cards\n')
        for card_name, card_data in card_imgs.items():
            # color_formatted_card_suit = f'{Fore.}'
            print(f"Card: {card_name}")
            for line in card_data.values():
                print(line)
            print()

    def print_texture(self, texture):
        for line_number in texture:
            print(texture[line_number])


if __name__ == "__main__":
    menu = Menu()
