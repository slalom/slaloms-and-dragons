import random
import curses
import game.story.elements.monster as monster
import game.story.elements.loot as loot
import game.story.elements.npc as npc
import game.story.elements.terrain.cave as cave
import game.story.elements.terrain.mountain as mountain


def generate():
    return map(10, 10)


__elements = {
    1: monster.build,
    2: loot.build,
    3: npc.build,
    4: cave.build,
    5: mountain.build
}


def __empty_builder():
    return {'type': 'empty', 'view': '🌱'}


def add_cell():
    random_number = random.randint(1, 20)
    builder = __elements.get(random_number, __empty_builder)
    return builder()


class map:

    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.model = [[add_cell() for x in range(x_dim)] for y in range(y_dim)]
        self.hero_position = (0, 0)
        self.model[self.hero_position[1]][self.hero_position[0]] = self.__traversed_cell()

    def __traversed_cell(self):
        return {'type':'empty', 'view': '🐾'}

    def move_hero(self, direction):
        if direction == curses.KEY_LEFT:
            new_x = self.hero_position[0] - 1
            if 0 <= new_x < self.x_dim:
                self.hero_position = (new_x, self.hero_position[1])
                temporary_cell = self.model[self.hero_position[1]][self.hero_position[0]]
                self.model[self.hero_position[1]][self.hero_position[0]] = self.__traversed_cell()
                return temporary_cell
        elif direction == curses.KEY_RIGHT:
            new_x = self.hero_position[0] + 1
            if 0 <= new_x < self.x_dim:
                self.hero_position = (new_x, self.hero_position[1])
                temporary_cell = self.model[self.hero_position[1]][self.hero_position[0]]
                self.model[self.hero_position[1]][self.hero_position[0]] = self.__traversed_cell()
                return temporary_cell
        elif direction == curses.KEY_UP:
            new_y = self.hero_position[1] - 1
            if 0 <= new_y < self.y_dim:
                self.hero_position = (self.hero_position[0], new_y)
                temporary_cell = self.model[self.hero_position[1]][self.hero_position[0]]
                self.model[self.hero_position[1]][self.hero_position[0]] = self.__traversed_cell()
                return temporary_cell
        elif direction == curses.KEY_DOWN:
            new_y = self.hero_position[1] + 1
            if 0 <= new_y < self.y_dim:
                self.hero_position = (self.hero_position[0], new_y)
                temporary_cell = self.model[self.hero_position[1]][self.hero_position[0]]
                self.model[self.hero_position[1]][self.hero_position[0]] = self.__traversed_cell()
                return temporary_cell

    def render(self, stdscr):
        for row_num, row in enumerate(self.model):
            for column_num, element in enumerate(row):
                if (column_num, row_num) == self.hero_position:
                    stdscr.addstr('🗡 ', curses.A_STANDOUT)
                else:
                    stdscr.addstr(element['view'].encode('UTF-8'))
            stdscr.addstr("\n")