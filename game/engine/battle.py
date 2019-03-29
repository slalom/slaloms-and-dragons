import game.engine.dice as dice

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
