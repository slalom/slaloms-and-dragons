import menu
import game

selection = menu.ask_for_selection()

if selection != '1':
    print('Beep boop')
else:
    game.start()
