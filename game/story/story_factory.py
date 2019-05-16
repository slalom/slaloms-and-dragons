import random
import game.story.elements.monster as monster
import game.story.elements.loot as loot
import game.story.elements.npc as npc
import game.story.elements.terrain.cave as cave
import game.story.elements.terrain.mountain as mountain
import game.map as map_model

def generate(story_length=3):
    library = [
        monster.build(),
        loot.build(),
        npc.build(),
        cave.build(),
        mountain.build()
    ]

    generate_map()

    return random.sample(library, k=story_length)

def generate_map():
    b = map_model.map(20, 50)
#     b.render()
