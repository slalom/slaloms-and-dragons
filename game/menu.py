import game.tools as tools

menu = [
    {
        'name': 'New Game',
    },
    {
        'name': 'Continue from where you left..'
    },
    {
        'name': 'How to play?'
    },
    {
        'name': 'Highscores'
    },
    {
        'name': 'Top Player'
    }
]


def ask_for_selection():
    return tools.show_picker(menu)
