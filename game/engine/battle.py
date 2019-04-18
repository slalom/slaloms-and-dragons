import game.engine.dice as dice
import game.engine.wait as wait


def fight(hero, monster):
    input('Hit [ENTER] to roll a die')
    hero_roll = dice.roll()
    print(f'You rolled {hero_roll}')
    hero_score = hero.strength + hero_roll

    monster_roll = dice.roll()
    print(f'{monster["name"]} rolled {monster_roll}')
    monster_score = monster['strength'] + monster_roll

    if hero_score > monster_score:
        print(f'You defeated {monster["name"]}')
    else:
        print(f'You were defeated by {monster["name"]}')
        print(f'You loose {monster_score - hero_score} hitpoints')
        hero.take_damage(monster_score - hero_score)
        wait.just_wait()

def threeRolls():
    roll_sum = 0
    print("To get through DEATH cave you must roll 3 times and get 12 or more.")
    input('Hit [ENTER] to roll a die')
    roll_1 = dice.roll()
    print(f'You rolled {roll_1}')
    roll_sum += roll_1

    input('Hit [ENTER] to roll a die')
    roll_2 = dice.roll()
    print(f'You rolled {roll_2}')
    roll_sum += roll_2

    input('Hit [ENTER] to roll a die')
    roll_3 = dice.roll()
    print(f'You rolled {roll_3}')
    roll_sum += roll_3

    if roll_sum >= 12:
        print('You have successfully crossed through DEATH cave.')
    else:
        print('You were defeated by DEATH cave')
        wait.just_wait()
        return False


def even_rolls():
    print("To get through mountain, you must roll even.")
    input('Hit [ENTER] to roll a die')
    roll = dice.roll()
    print(f'You rolled {roll}')

    if roll % 2 == 0:
        print('You have successfully climbed Zagros Montain.')
    else:
        print('You were defeated by Zagros Mountain')
        wait.just_wait()
        hero.die()
