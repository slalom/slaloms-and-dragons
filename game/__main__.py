import game.menu as menu
import game.game as game
import emoji
import sys
import time
import pyfiglet
from colored import fg, bg, attr


color = fg('orchid')
reset = attr('reset')
bold = attr('bold')
result = pyfiglet.figlet_format("SLALOM & DRAGONS")
print(color + result + reset)

animation = emoji.emojize(
    "%s%sLet's play SLALOM & DRAGONS%s :dragon:" %
    (color, bold, reset))

for i in animation:
    time.sleep(0.1)
    sys.stdout.write(i)
    sys.stdout.flush()
print("\n")

selection = menu.ask_for_selection()

if selection != '1':
    print('Beep boop')
else:
    game.start()
