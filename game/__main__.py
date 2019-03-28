import game.menu as menu
import game.game as game
import emoji
import sys
import time
import pyfiglet
from colorama import Fore, Back, Style


color = Fore.MAGENTA
font_bold = Style.BRIGHT
result = pyfiglet.figlet_format("SLALOMS & DRAGONS")
print(color + font_bold + result)

animation = emoji.emojize(color + font_bold +
                          "Let's play SLALOMS & DRAGONS :dragon:")

for i in animation:
    time.sleep(0.1)
    sys.stdout.write(i)
    sys.stdout.flush()
print("\n")
print(Style.RESET_ALL)

selection = menu.ask_for_selection()

if selection != '1':
    print('Beep boop')
else:
    game.start()
