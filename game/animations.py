import emoji
import sys
import time
import pyfiglet
from colorama import Fore, Back, Style

title = "slaloms & dragons"
subtitle = "Let's play SLALOMS & DRAGONS :dragon:"


def show_intro():
    color = Fore.MAGENTA
    font_bold = Style.BRIGHT
    result = pyfiglet.figlet_format(" ".join(list(title.upper())), font="mini")
    print(color + font_bold + result)

    animation = emoji.emojize(color + font_bold + subtitle)

    for i in animation:
        time.sleep(0.03)
        sys.stdout.write(i)
        sys.stdout.flush()
    print("\n")
    print(Style.RESET_ALL)
