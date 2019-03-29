import game.menu as menu
import game.game as game
import game.animations as animations

animations.show_intro()

selection = menu.ask_for_selection()

if selection != 'New Game':
    print('Beep boop')
else:
    game.start()
