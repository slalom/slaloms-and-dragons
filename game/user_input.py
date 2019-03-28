from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2


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

def get():
    user_input = '0'
    answer = prompt(questions, style=custom_style_2)
    if answer['option'] == 'New Game':
        user_input = '1'
    return user_input

