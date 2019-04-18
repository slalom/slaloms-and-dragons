import game.story.welcome as welcome
import game.story.end as end
import game.story.story_factory as story_factory
import game.character.creator as character_creator
import game.engine.wait as wait

import game.character.character as character
import game.progression.ability as ability
import game.engine.step_engine as step_engine

def play_step(step, hero):
    step_type = step.get('type')
    return step_engine.forType(step_type)(step, hero)

def start():
    welcome.show()
    hero = character_creator.new()
    hero.print_character()
    ability_track = ability.get_ability(hero)

    story = story_factory.generate()
    won = True
    
    print()
    print('Lets begin ')
    print()
    for step in story:
        wait.step_wait()
        result = play_step(step, hero)
        if not result:
            won = False
            break
    end.show(win=won)
