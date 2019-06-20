import game.engine.dice as dice
import game.engine.wait as wait


def fight(hero, monster, stdscr):
    stdscr.addstr("Hit [ENTER] to roll a die\n")
    stdscr.getkey()
    hero_roll = dice.roll()
    stdscr.addstr(f"You rolled {hero_roll}. ")
    hero_score = hero.strength + hero_roll

    monster_roll = dice.roll()
    stdscr.addstr(f'{monster["name"]} rolled {monster_roll}. ')
    monster_score = monster["strength"] + monster_roll

    if hero_score > monster_score:
        stdscr.addstr(f'You defeated {monster["name"]}!')
    else:
        stdscr.addstr(f'You were defeated by {monster["name"]}. ')
        stdscr.addstr(f"You lose {monster_score - hero_score} hitpoints. ")
        hero.take_damage(monster_score - hero_score)
        wait.just_wait()


def threeRolls(stdscr):
    roll_sum = 0
    stdscr.addstr(
        "To get through DEATH cave you must roll \n3 times and get 12 or more.\n"
    )
    stdscr.addstr("Hit [ENTER] to roll a die\n")
    stdscr.getkey()
    roll_1 = dice.roll()
    stdscr.addstr(f"You rolled {roll_1}\n")
    roll_sum += roll_1

    stdscr.addstr("Hit [ENTER] to roll a die\n")
    stdscr.getkey()
    roll_2 = dice.roll()
    stdscr.addstr(f"You rolled {roll_2}\n")
    roll_sum += roll_2

    stdscr.addstr("Hit [ENTER] to roll a die\n")
    stdscr.getkey()
    roll_3 = dice.roll()
    stdscr.addstr(f"You rolled {roll_3}\n")
    roll_sum += roll_3

    if roll_sum >= 12:
        stdscr.addstr("You have successfully crossed through DEATH cave.\n")
    else:
        stdscr.addstr("You were defeated by DEATH cave\n")
        wait.just_wait()
        return False


def even_rolls(hero, stdscr):
    stdscr.addstr("To get through mountain, you must roll even.\n")
    stdscr.addstr("Hit [ENTER] to roll a die\n")
    stdscr.getkey()
    roll = dice.roll()
    stdscr.addstr(f"You rolled {roll}\n")

    if roll % 2 == 0:
        stdscr.addstr("You have successfully climbed Zagros Montain.\n")
    else:
        stdscr.addstr("You were defeated by Zagros Mountain\n")
        wait.just_wait()
        hero.die()
