import game.tools as tools


class map:

    def __init__(self, matrix, name):
        self.matrix = matrix
        self.name = name

    def render(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                #print(matrix[i][j])
                print('.')
            print()
        


