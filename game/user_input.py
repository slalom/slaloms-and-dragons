from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2


questions = [
    {
        'type': 'checkbox',
        'qmark': '🐉 ⚔️ ',
        'message': 'Select a choice',
        'name': 'option',
        'choices': [
            Separator('= Play a game ='),
            {
                'name': 'New Game'
            },
            {
                'name': 'Continue from where you left..'
            },
            Separator('= Help ='),
            {
                'name': 'How to play?'
            },
            Separator('= Highscores ='),
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
    if len(answer['option']) >= 2:
        print('OOPS.. you can only select one option')
        return
    elif len(answer['option']) == 0:
        print('You forgot to select an option')
        return
    else:
        if answer['option'][0] == 'New Game':
            user_input = '1'
        return user_input

