import game.progression.power as Power


def get_ability(character):
    print('\n')
    print('Lets see your powers', character.name, ":")
    power = Power.power()
    for power in power.GetPower():
        print(power)
    print()
