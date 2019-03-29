import random
import time
import game.character.character as character


def new():
    properties = {"race": "", "gender": ""}
    valid_race = ["Human", "Elf", "Dwarf"]
    valid_gender = ["Male", "Female", "Other"]
    properties["name"] = input("Please input your adventurer's name:")
    while properties["race"] not in valid_race:
        properties["race"] = input(
            "Please input your race 'Human, Elf, or Dwarf':")
        if properties["race"] not in valid_race:
            print("Your options are 'Human, Elf, or Dwarf'")
    while properties["gender"] not in valid_gender:
        properties["gender"] = input(
            "Please input your gender 'Male, Female, or Other':")
        if properties["gender"] not in valid_gender:
            print("Your options are 'Male, Female, or Other'")
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
