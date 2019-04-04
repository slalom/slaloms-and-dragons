import game.story.welcome as welcome
import game.story.end as end
import game.story.story_factory as story_factory
import game.character.creator as character_creator
import game.npc as npc
import game.engine.wait as wait
import game.engine.battle as battle
import game.character.character as character
import game.progression.ability as ability

def play_step(step, hero):
    print()
    print('Lets begin ')
    print()
    step_type = step.get('type')

    if step_type == 'monster':
        monster = step['monster']
        print(
            f'You encounter a monster! It is a {monster["name"]} with a strength of {monster["strength"]}')
        battle.fight(hero, monster)
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
    if step_type == 'mountain':
        mtn = step.get('mountain')
        print(mtn["greeting"])
        battle.even_rolls()

    if step_type == 'cave':
        cave = step.get('cave')
        print(cave["greeting"])
        battle.threeRolls()


def start():
    welcome.show()

    hero = character_creator.new()
    hero.print_character()
    ability_track = ability.get_ability(hero)

    story = story_factory.generate()
    for step in story:
        wait.step_wait()
        play_step(step, hero)
    end.show()
