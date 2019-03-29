import random
import time
import game.character.character as character
import game.tools as tools


def new():
    properties = {}
    properties["name"] = input("Please input your adventurer's name:")

    print('Select your race')
    race = tools.show_picker([{'name': 'Human'}, {'name': 'Elf'}, {'name': 'Dwarf'}])
    properties['race'] = race['option']
    
    print('Select your gender')
    race = tools.show_picker([{'name': 'Male'}, {'name': 'Female'}, {'name': 'Other'}])
    properties['gender'] = race['option']

    print()
    print("Rolling ability scores")
    # "\r" takes the cursor to the beginning of the line
    simulate_pause = r"/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\| "
    for i in simulate_pause:
        print("\r", i, end="")
        time.sleep(.04)
    print()
    properties["strength"] = random.randint(3, 18)
    properties["dexterity"] = random.randint(3, 18)
    properties["constitution"] = random.randint(3, 18)
    properties["hitpoints"] = 10

    return character.Character(properties)
