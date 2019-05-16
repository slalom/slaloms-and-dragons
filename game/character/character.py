#test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20, "inventory": [], "level":0, "experience":560}


class Character:
    def __init__(self, character):
        '''
        character: dictionary passed from create_character function
        '''
        self.name = character["name"]
        self.race = character["race"]
        self.gender = character["gender"]
        self.strength = character["strength"]
        self.dexterity = character["dexterity"]
        self.constitution = character["constitution"]
        self.hitpoints = character["hitpoints"]
        self.inventory = character["inventory"]
        self.experience = character["experience"]
        self.level = character["level"]

    def print_character(self):
        '''
        prints: character attributes
        '''
        print("Slalom & Dragons Character Information:")
        print("---------------------------------------")
        print("Name:", self.name)
        print("Race:", self.race)
        print("Gender:", self.gender)
        print("Strength:", self.strength)
        print("Dexterity:", self.dexterity)
        print("Constitution:", self.constitution)
        print("Hitpoints:", self.hitpoints)
        print("inventory:", self.inventory)
        print("Experience:", self.experience)
        print("Level:", self.level)

    def calc_level(self):
        calc_level = self.experience // 100
        if calc_level > self.level:
            #self.level_up()
            pass
        self.level = calc_level

    def pickup(self, trophy):
        print('Sweet!')

    def add_inventory(self, item):
        self.inventory.append(item)
        print("inventory:", self.inventory)

        # add to inventory

    def take_damage(self, damage):
        self.hitpoints -= damage

    def die(self):
        self.hitpoints = 0

    def is_alive(self):
        return self.hitpoints > 0

    def __str__(self):
        string = "Class: Character\nCharacter Name: " + self.name
        return string

#character = Character(test_character)
#character.calc_level()
#character.print_character()

