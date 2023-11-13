# import colorama
from colorama import Fore, Style

blank_card = {
    0: '┌───────┐',
    1: '│       │',
    2: '│       │',
    3: '│   ?   │',
    4: '│       │',
    5: '│       │',
    6: '└───────┘'
}

card_imgs = {
    'blank_card': {
        0: '┌───────┐',
        1: '│       │',
        2: '│       │',
        3: '│   ?   │',
        4: '│       │',
        5: '│       │',
        6: '└───────┘',
    },
    'A♦': {
        0: '┌───────┐',
        1: f'│A{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     A{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '2♦': {
        0: '┌───────┐',
        1: f'│2{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     2{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '3♦': {
        0: '┌───────┐',
        1: f'│3{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     3{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '4♦': {
        0: '┌───────┐',
        1: f'│4{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     4{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '5♦': {
        0: '┌───────┐',
        1: f'│5{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     5{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '6♦': {
        0: '┌───────┐',
        1: f'│6{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     6{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '7♦': {
        0: '┌───────┐',
        1: f'│7{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     7{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '8♦': {
        0: '┌───────┐',
        1: f'│8{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     8{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '9♦': {
        0: '┌───────┐',
        1: f'│9{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     9{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    '10♦': {
        0: '┌───────┐',
        1: f'│10{Fore.RED}♦{Fore.WHITE}    │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│    10{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    'J♦': {
        0: '┌───────┐',
        1: f'│J{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     J{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    'Q♦': {
        0: '┌───────┐',
        1: f'│Q{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     Q{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    'K♦': {
        0: '┌───────┐',
        1: f'│K{Fore.RED}♦{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♦{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     K{Fore.RED}♦{Fore.WHITE}│',
        6: '└───────┘',
    },
    'A♠': {
        0: '┌───────┐',
        1: f'│A{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     A{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '2♠': {
        0: '┌───────┐',
        1: f'│2{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     2{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '3♠': {
        0: '┌───────┐',
        1: f'│3{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     3{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '4♠': {
        0: '┌───────┐',
        1: f'│4{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     4{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '5♠': {
        0: '┌───────┐',
        1: f'│5{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     5{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '6♠': {
        0: '┌───────┐',
        1: f'│6{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     6{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '7♠': {
        0: '┌───────┐',
        1: f'│7{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     7{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '8♠': {
        0: '┌───────┐',
        1: f'│8{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     8{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '9♠': {
        0: '┌───────┐',
        1: f'│9{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     9{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '10♠': {
        0: '┌───────┐',
        1: f'│10{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}    │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│    10{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'J♠': {
        0: '┌───────┐',
        1: f'│J{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     J{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'Q♠': {
        0: '┌───────┐',
        1: f'│Q{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     Q{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'K♠': {
        0: '┌───────┐',
        1: f'│K{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     K{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'A♥': {
        0: '┌───────┐',
        1: f'│A{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     A{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '2♥': {
        0: '┌───────┐',
        1: f'│2{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     2{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '3♥': {
        0: '┌───────┐',
        1: f'│3{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     3{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '4♥': {
        0: '┌───────┐',
        1: f'│4{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     4{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '5♥': {
        0: '┌───────┐',
        1: f'│5{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     5{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '6♥': {
        0: '┌───────┐',
        1: f'│6{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     6{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '7♥': {
        0: '┌───────┐',
        1: f'│7{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     7{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '8♥': {
        0: '┌───────┐',
        1: f'│8{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     8{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '9♥': {
        0: '┌───────┐',
        1: f'│9{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     9{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    '10♥': {
        0: '┌───────┐',
        1: f'│10{Fore.RED}♥{Fore.WHITE}    │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│    10{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    'J♥': {
        0: '┌───────┐',
        1: f'│J{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     J{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    'Q♥': {
        0: '┌───────┐',
        1: f'│Q{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     Q{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    'K♥': {
        0: '┌───────┐',
        1: f'│K{Fore.RED}♥{Fore.WHITE}     │',
        2: '│       │',
        3: f'│   {Fore.RED}♥{Fore.WHITE}   │',
        4: '│       │',
        5: f'│     K{Fore.RED}♥{Fore.WHITE}│',
        6: '└───────┘',
    },
    'A♣': {
        0: '┌───────┐',
        1: f'│A{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     A{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '2♣': {
        0: '┌───────┐',
        1: f'│2{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     2{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '3♣': {
        0: '┌───────┐',
        1: f'│3{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     3{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '4♣': {
        0: '┌───────┐',
        1: f'│4{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     4{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '5♣': {
        0: '┌───────┐',
        1: f'│5{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     5{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '6♣': {
        0: '┌───────┐',
        1: f'│6{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     6{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '7♣': {
        0: '┌───────┐',
        1: f'│7{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     7{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '8♣': {
        0: '┌───────┐',
        1: f'│8{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     8{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '9♣': {
        0: '┌───────┐',
        1: f'│9{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     9{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    '10♣': {
        0: '┌───────┐',
        1: f'│10{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}    │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│    10{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'J♣': {
        0: '┌───────┐',
        1: f'│J{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     J{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'Q♣': {
        0: '┌───────┐',
        1: f'│Q{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     Q{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
    'K♣': {
        0: '┌───────┐',
        1: f'│K{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │',
        2: '│       │',
        3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │',
        4: '│       │',
        5: f'│     K{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}│',
        6: '└───────┘',
    },
}
