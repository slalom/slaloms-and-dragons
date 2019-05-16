import random
import game.story.builders as builders
import game.map as map_model

def generate(story_length=3):
    library = [
        builders.monster(),
        builders.trophy('The Sword of Damocles', 10),
        builders.npc('Mary', 'human'),

        {'type': 'mountain',
         'mountain': {'name': 'Zagros',
                      'greeting': 'You have arrived at Zagros mountain. The largest mountian in all of Kurdistan. Will you climb it?'}},

        {'type': 'cave',
         'cave': {'greeting': 'You have arrived at the deepest darkest cave, DEATH cave. Will you enter?'}}
    ]

    generate_map()

    return random.sample(library, k=story_length)

def generate_map():
    b = map_model.map(20, 50)
#     b.render()
