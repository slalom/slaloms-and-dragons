import game.engine.battle as battle
import game.npc as npc_character


def forType(step_type):
    if step_type == 'monster':
        return monster
    if step_type == 'loot':
        return loot
    if step_type == 'npc':
        return npc
    if step_type == 'mountain':
        return mountain
    if step_type == 'cave':
        return cave


def monster(step, hero, stdscr):
    monster = step['monster']
    stdscr.addstr(
        f'You encounter a monster! It is a {monster["name"]} with a strength of {monster["strength"]}\n')
    battle.fight(hero, monster, stdscr)


def loot(step, hero, stdscr):
    item = step['loot']
    stdscr.addstr(f'You found something! Ahhh! It is the {item["name"]}!')
    hero.pickup(item)

def npc(step, hero, stdscr):
    npm_spec = step['npc']
    stdscr.addstr('You see someone in the shadows...')
    mary = npc_character.npc(npm_spec['name'], npm_spec['npc_class'],
                             npm_spec['greeting'])
    mary.meet()


def mountain(step, hero, stdscr):
    mtn = step.get('mountain')
    stdscr.addstr(mtn["greeting"] + "\n")
    if not battle.even_rolls(hero, stdscr):
        hero.die()


def cave(step, hero, stdscr):
    cave = step.get('cave')
    stdscr.addstr(cave["greeting"] + "\n")
    if not battle.threeRolls(stdscr):
        hero.die()
