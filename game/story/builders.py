import game.story.monster.name as monster_names
import random

def monster():
    return {'type': 'monster', 'monster': {'name': monster_names.generate(),
                                           'strength': random.randint(1, 10)}}


def trophy(name, value):
    return {'type': 'trophy', 'trophy': {'name': name,
                                         'value': value}}


def npc(name, clazz):
    return {
        'type': 'npc',
        'npc': {
            'name': name,
            'npc_class': clazz,
            'greeting': f'Well hello there! My name is {name}. Can you help me??'}}
