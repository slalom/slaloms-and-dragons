import game.tools as tools
import random

monster_ratio = 0.1
treasure_ratio = 0.1
encounter_ratio = 0.1

def add_cell():
    random_number = random.randint(1, 10)
    if random_number == 1:
        return 'M'
    elif random_number == 2:
        return 'T'
    elif random_number == 3:
        return 'E'
    else:
        return " "


class map:

    def __init__(self, x_dim, y_dim):
        self.model = [[add_cell() for y in range(y_dim)] for x in range(x_dim)]
    
    def render(self):
        print("-"*(len(self.model[0]) +2))
        for row in self.model:
            print("|", end="")
            for column in row:
                print(column, end="")
            print("|")
        print("-"*(len(self.model[0]) +2))
