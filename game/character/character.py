#test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20}


class Character:
    def __init__(self, character):
        self.name = character["name"]
        self.race = character["race"]
        self.gender = character["gender"]
        self.strength = character["strength"]
        self.dexterity = character["dexterity"]
        self.constitution = character["constitution"]
        self.hitpoints = character["hitpoints"]

    def pickup(self, trophy):
        print('Sweet!')
        # add to inventory

#character = Character(test_character)
#print("Character Name:", character.name)
#print("Character race:", character.race)
