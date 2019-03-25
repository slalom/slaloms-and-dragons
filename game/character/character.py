#test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20}

import random


class Character:
    def __init__(self, character):
        self.name = character["name"]
        self.race = character["race"]
        self.gender = character["gender"]
        self.strength = character["strength"]
        self.dexterity = character["dexterity"]
        self.constitution = character["constitution"]
        self.hitpoints = character["hitpoints"]

    def fight(self, monster):
        hero_score = self.strength + random.randint(1, 6)
        monster_score = monster['strength'] + random.randint(1, 6)
        monster_name = monster['name']

        if hero_score > monster_score:
            print(f'You defeated {monster_name}')
        else:
            print(f'You were defeated by {monster_name}')

    def pickup(self, trophy):
        print('Sweet!')
        # add to inventory

#character = Character(test_character)
#print("Character Name:", character.name)
#print("Character race:", character.race)
