import game.plot.welcome as welcome
import game.plot.end as end
import game.plot.story_factory as story_factory
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


def start():
    welcome.show()
    hero = character_creator.new()
    story = story_factory.generate()
    new_character = character.create_character()
    character_instance = character.Character(new_character)
    character_instance.print_character()
    ability_track = ability.get_ability(new_character)
    for step in story:
        wait.wait_with_animation()
        play_step(step, hero)
    end.show()
