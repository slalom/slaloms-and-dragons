import PyInquirer
import examples

questions = [
    {
        'type': 'list',
        'qmark': '🐉 ⚔️ ',
        'message': 'Select a choice',
        'name': 'option',
        'choices': [
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
    }
]

def ask_for_selection():
    return PyInquirer.prompt(questions, style=examples.custom_style_3)
