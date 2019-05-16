import game.tools as tools

class map:

    def __init__(self, size):
        self.model = [[" " for y in range(size)] for x in range(size)]

    def render(self):
        print("-"*(len(self.model[0]) +2))
        for row in self.model:
            print("|", end="")
            for column in row:
                print(column, end="")
            print("|")
        print("-"*(len(self.model[0]) +2))
