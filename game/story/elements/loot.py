import random

def build():
    return {'type': 'trophy', 'trophy': {'name': random.choice(__names),
                                         'value': random.randint(1, 10)}}
                                        
__names = ['The Sword of Damocles']