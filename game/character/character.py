import random
import time


# test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20}

def create_character():
    '''
    returns: dictionary, character attributes
    '''
    character = {"race": "", "gender": ""}
    valid_race = ["Human", "Elf", "Dwarf"]
    valid_gender = ["Male", "Female", "Other"]
    character["name"] = input("Please input your adventurer's name:")
    while character["race"] not in valid_race:
        character["race"] = input(
            "Please input your race 'Human, Elf, or Dwarf':")
        if character["race"] not in valid_race:
            print("Your options are 'Human, Elf, or Dwarf'")
    while character["gender"] not in valid_gender:
        character["gender"] = input(
            "Please input your gender 'Male, Female, or Other':")
        if character["gender"] not in valid_gender:
            print("Your options are 'Male, Female, or Other'")
    print()
    print("Rolling ability scores")
    # "\r" takes the cursor to the beginning of the line
    simulate_pause = r"/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\| "
    for i in simulate_pause:
        print("\r", i, end="")
        time.sleep(.04)
    print()
    character["strength"] = random.randint(3, 18)
    character["dexterity"] = random.randint(3, 18)
    character["constitution"] = random.randint(3, 18)
    character["hitpoints"] = 10
    return character


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

    def pickup(self, trophy):
        print('Sweet!')
        # add to inventory

    def __str__(self):
        string = "Class: Character\nCharacter Name: " + self.name
        return string

# character = Character(test_character)
# print("Character Name:", character.name)
# print("Character race:", character.race)

# adventurer = Character(create_character())
# adventurer.print_character()
