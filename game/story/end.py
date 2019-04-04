import game.story.game_over as game_over 

def show(win=True):
    if win: 
        print('\n🔥🔥 You Win 🔥🔥')
    else: 
        game_over.play_game_over() 
