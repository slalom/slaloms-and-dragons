def monster(name, strength):
    return {'type': 'monster', 'monster': {'name': name,
                                           'strength': strength}}


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
