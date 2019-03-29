import random
import game.engine.wait as wait


def roll():
    wait.roll_wait()
    return random.randint(1, 6)
