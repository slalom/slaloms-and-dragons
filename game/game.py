from curses import wrapper
import locale

import game.story.welcome as welcome
import game.story.end as end
import game.story.map_factory as map_factory
import game.character.creator as character_creator
import game.engine.wait as wait

import game.character.character as character
import game.progression.ability as ability
import game.engine.step_engine as step_engine


def play_step(step, hero, stdscr):
    stdscr.refresh()
    if step and step['type'] != 'empty':
        step_engine.forType(step.get('type'))(step, hero, stdscr)


def start():
    welcome.show()
    map = map_factory.generate()
    hero = character_creator.new()
    hero.print_character()
    wrapper(loop, map, hero)
    end.show(win=False)


def loop(stdscr, map, hero):
    locale.setlocale(locale.LC_ALL, '')
    map.render(stdscr)
    while hero.is_alive():
        direction = stdscr.getch()
        stdscr.clear()
        step = map.move_hero(direction)
        map.render(stdscr)
        play_step(step, hero, stdscr)
