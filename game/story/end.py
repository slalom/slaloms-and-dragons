import game.story.game_over as game_over
from colorama import Fore, Back, Style
import emoji
import sys
import time


def show(win=True):
    if win:
        print('\n🔥🔥 You Win 🔥🔥')
    else:
        color = Fore.RED
        font_bold = Style.BRIGHT
        death = 'AAAAAAAAAAHAHHHHHHHHHAHAAARRRRRRRRRRRRRGRRGGGGGGGGRHHHHHHHHHHHH'
        animation = emoji.emojize(color + font_bold + death)
        for i in animation:
            time.sleep(0.05)
            sys.stdout.write(i)
            sys.stdout.flush()
        print('\n')
        print(Style.RESET_ALL)

        game_over.play_game_over()
