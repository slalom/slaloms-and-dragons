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
    wrapper(loop, map, hero)
    end.show(win=False)


def loop(stdscr, map, hero): 
    locale.setlocale(locale.LC_ALL, '')
    map_window = stdscr.derwin(15, 25, 1, 1)
    map_window.keypad(True)
    character_window = stdscr.derwin(15, 60, 1, 28)
    text_window = stdscr.derwin(5, 60, 16, 28)
    stdscr.vline(1,27,'|', 15)

    map.render(map_window)
    while hero.is_alive():
        hero.print_character(character_window)
        text_window.refresh()
        character_window.refresh()
        direction = map_window.getch()
        text_window.clear()
        character_window.clear()
        map_window.clear()
        step = map.move_hero(direction)
        map.render(map_window)
        play_step(step, hero, text_window)
