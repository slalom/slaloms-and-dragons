import game.story.welcome as welcome
import game.story.end as end
import game.story.story_factory as story_factory
import game.character.creator as character_creator
import game.engine.wait as wait

import game.character.character as character
import game.progression.ability as ability
import game.engine.step_engine as step_engine
import game.sound as sound


def play_step(step, hero):
    return step_engine.forType(step.get('type'))(step, hero)


def start():
    sound.play_music()
    welcome.show()
    story = story_factory.generate()
    hero = character_creator.new()
    hero.print_character()
    ability_track = ability.get_ability(hero)

    won = True

    for step in story:
        wait.step_wait()
        play_step(step, hero)
        if not hero.is_alive():
            won = False
            break
    end.show(win=won)
