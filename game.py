import plot.welcome
import plot.end
import plot.story_factory
import character.creator
import engine.step_handler
import npc


def play_step(step, hero):
    step_type = step.get('type')
    if step_type == 'monster':
        monster = step['monster']
        hero.fight(monster)
    if step_type == 'trophy':
        trophy = step['trophy']
        engine.step_handler.pickup(hero, trophy)
    if step_type == 'npc':
        npm_spec = step['npc']
        mary = npc.npc(npm_spec['name'], npm_spec['npc_class'],
                       npm_spec['greeting'])
        mary.meet()


def start():
    plot.welcome.show()
    hero = character.creator.new()
    story = plot.story_factory.generate()
    for step in story:
        play_step(step, hero)
    plot.end.show()
