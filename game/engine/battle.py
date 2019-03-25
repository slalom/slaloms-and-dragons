import game.engine.dice as dice
import game.engine.wait as wait


def fight(hero, monster):
    input('Hit [ENTER] to roll a die')
    wait.wait_with_animation()
    hero_roll = dice.roll()
    print(f'You rolled {hero_roll}')
    hero_score = hero.strength + hero_roll

    wait.wait_with_animation()
    monster_roll = dice.roll()
    print(f'{monster["name"]} rolled {monster_roll}')
    monster_score = monster['strength'] + monster_roll

    if hero_score > monster_score:
        print(f'You defeated {monster["name"]}')
    else:
        print(f'You were defeated by {monster["name"]}')
