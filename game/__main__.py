import game.menu as menu
import game.game as game
import emoji
import sys
import time


animation = emoji.emojize("Let's play SLALOM & DRAGONS :dragon:")

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
