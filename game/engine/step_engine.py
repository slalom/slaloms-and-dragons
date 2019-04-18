import game.engine.battle as battle
import game.npc as npc_character

def forType(step_type):
    if step_type == 'monster':
        return monster
    if step_type == 'trophy':
        return trophy
    if step_type == 'npc':
        return npc
    if step_type == 'mountain':
        return mountain
    if step_type == 'cave':
        return cave

def monster(step, hero):
    monster = step['monster']
    print(
        f'You encounter a monster! It is a {monster["name"]} with a strength of {monster["strength"]}')
    return battle.fight(hero, monster)

def trophy(step, hero):
    trophy = step['trophy']
    print(
        f'You found something! Ahhh! It is the {trophy["name"]}!')
    return hero.pickup(trophy)

def npc(step, hero):
    npm_spec = step['npc']
    print('You see someone in the shadows...')
    mary = npc_character.npc(npm_spec['name'], npm_spec['npc_class'],
                   npm_spec['greeting'])
    return mary.meet()

def mountain(step, hero):
    mtn = step.get('mountain')
    print(mtn["greeting"])
    if not battle.even_rolls(hero):
        hero.die()

def cave(step, hero):
    cave = step.get('cave')
    print(cave["greeting"])
    if not battle.threeRolls():
        hero.die()