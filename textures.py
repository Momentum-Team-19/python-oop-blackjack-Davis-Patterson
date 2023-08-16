import colorama
from colorama import Fore

card_img = {
    0: '┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐',
    1: f'│J{Fore.BLUE}♣{Fore.WHITE}     │  │Q{Fore.RED}❤{Fore.WHITE}     │  │K{Fore.BLUE}♠{Fore.WHITE}     │  │A{Fore.RED}♦{Fore.WHITE}     │',
    2: '│       │  │       │  │       │  │       │',
    3: f'│   {Fore.BLUE}♣{Fore.WHITE}   │  │   {Fore.RED}❤{Fore.WHITE}   │  │   {Fore.BLUE}♠{Fore.WHITE}   │  │   {Fore.RED}♦{Fore.WHITE}   │',
    4: '│       │  │       │  │       │  │       │',
    5: f'│    {Fore.BLUE}♣{Fore.WHITE} J│  │    {Fore.RED}❤{Fore.WHITE} Q│  │    {Fore.BLUE}♠{Fore.WHITE} K│  │    {Fore.RED}♦{Fore.WHITE} A│',
    6: '└───────┘  └───────┘  └───────┘  └───────┘',
}

texture1 = {
    0: '_|_     _|_     _|_     _|_     _|_     _|_',
    1: ' |       |       |       |       |       | ',
    2: '    _|_     _|_     _|_     _|_     _|_    ',
    3: '     |       |       |       |       |     '
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

# {Fore.BLUE}♠{Fore.WHITE}
# {Fore.RED}❤{Fore.WHITE}
# {Fore.BLUE}♣{Fore.WHITE}
# {Fore.RED}♦{Fore.WHITE}
