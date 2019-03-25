#test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20}

import game.engine.dice as dice
import game.engine.wait as wait

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
        input('Hit [ENTER] to roll a die')
        wait.wait_with_animation()
        hero_roll = dice.roll()
        print(f'You rolled {hero_roll}')
        hero_score = self.strength + hero_roll
        
        wait.wait_with_animation()
        monster_roll = dice.roll()
        print(f'{monster["name"]} rolled {monster_roll}')
        monster_score = monster['strength'] + monster_roll

        if hero_score > monster_score:
            print(f'You defeated {monster["name"]}')
        else:
            print(f'You were defeated by {monster["name"]}')

    def pickup(self, trophy):
        print('Sweet!')
        # add to inventory

#character = Character(test_character)
#print("Character Name:", character.name)
#print("Character race:", character.race)
