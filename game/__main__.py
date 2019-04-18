import game.menu as menu
import game.game as game
import game.animations as animations
import game.help as helper

animations.show_intro()

selection = menu.ask_for_selection()

if selection == 'New Game':
    game.start()
elif selection == 'How to play?':
    helper.guide()
else:
    print('Beep boop')
