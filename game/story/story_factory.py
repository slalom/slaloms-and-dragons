import random
import game.story.builders as builders


def generate(story_length=3):
    library = [
        builders.monster('Chupacabra', 5),
        builders.trophy('The Sword of Damocles', 10),
        builders.npc('Mary', 'human'),

        {'type': 'mountain',
         'mountain': {'name': 'Zagros',
                      'greeting': 'You have arrived at Zagros mountain. The largest mountian in all of Kurdistan. Will you climb it?'}},

        {'type': 'cave',
         'cave': {'greeting': 'You have arrived at the deepest darkest cave, DEATH cave. Will you enter?'}}
    ]

    return random.sample(library, k=story_length)
