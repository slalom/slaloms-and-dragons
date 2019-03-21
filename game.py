import plot.welcome
import plot.end
import plot.story_factory
import character.creator
import npc


def play_step(step, hero):
    print()
    step_type = step.get('type')
    if step_type == 'monster':
        monster = step['monster']
        print(
            f'You encounter a monster! It is a {monster["name"]} with a strength of {monster["strength"]}')
        hero.fight(monster)
    if step_type == 'trophy':
        trophy = step['trophy']
        print(f'You found something! Ahhh! It is the {trophy["name"]}!')
        hero.pickup(trophy)
    if step_type == 'npc':
        npm_spec = step['npc']
        print('You see someone in the shadows...')
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
