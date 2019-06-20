import game.tools as tools

menu = [
    "New Game",
    "Continue from where you left..",
    "How to play?",
    "Highscores",
    "Top Player",
]


def ask_for_selection():
    return tools.show_picker(menu)
