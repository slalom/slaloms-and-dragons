from .power import Power


powers = []
special_power = ""


def get_ability(character):
    print('\n')
    print('Lets see your powers', character.name, ":")
    get_powers(character)


def get_powers(character):

    if character.race == "Human":
        powers = ["Sword", "Knife"]
        special_power = "I can speak to dragons"
        print('You can fight well with: ')
        print(powers[0], '⚔️')
        print(powers[1], '🗡️')
        print(special_power, '🐉')
        print()
