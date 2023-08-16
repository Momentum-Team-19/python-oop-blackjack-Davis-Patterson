import colorama
from colorama import Fore, Style

cards_txt = {
    0: '┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐',
    1: f'│J{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}     │  │Q{Fore.RED}❤{Fore.WHITE}     │  │K{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}     │  │A{Fore.RED}♦{Fore.WHITE}     │',
    2: '│       │  │       │  │       │  │       │',
    3: f'│   {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}   │  │   {Fore.RED}❤{Fore.WHITE}   │  │   {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}   │  │   {Fore.RED}♦{Fore.WHITE}   │',
    4: '│       │  │       │  │       │  │       │',
    5: f'│    {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL} J│  │    {Fore.RED}❤{Fore.WHITE} Q│  │    {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL} K│  │    {Fore.RED}♦{Fore.WHITE} A│',
    6: '└───────┘  └───────┘  └───────┘  └───────┘',
}

# card_img = {
#     0: '┌───────┐',
#     1: f'│{ }     │',
#     2: '│       │',
#     3: f'│  { }   │',
#     4: '│       │',
#     5: f'│     { }│',
#     6: '└───────┘',
# }

texture1 = {
    0: '_|_     _|_     _|_     _|_     _|_     _|_',
    1: ' |       |       |       |       |       | ',
    2: '    _|_     _|_     _|_     _|_     _|_    ',
    3: '     |       |       |       |       |     '
}

texture2 = {
    0: '',
    1: '',
    2: '',
    3: ''
}

# card_img = {
#     1: '┌─────────┐    ┌─────────┐',
#     2: '│A♠       │    │K❤       │',
#     3: '│         │    │         │',
#     4: '│         │    │         │',
#     5: '│    ♠    │    │    ❤    │',
#     6: '│         │    │         │',
#     7: '│         │    │         │',
#     8: '│       ♠A│    │      ❤ K│',
#     9: '└─────────┘    └─────────┘',
# }

# {Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}
# {Fore.RED}❤{Fore.WHITE}
# {Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}
# {Fore.RED}♦{Fore.WHITE}
