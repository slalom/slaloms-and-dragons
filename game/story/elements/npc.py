import random


def build():
    name = random.choice(__names)
    return {
        'type': 'npc',
        'npc': {
            'name': name,
            'npc_class': 'human',
            'greeting': f'Well hello there! My name is {name}. Can you help me??'},
        # 'view': '🙋‍'}
        'view': '👸'}


__names = ['Mary']
