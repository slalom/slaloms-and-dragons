import random

def fight(character, monster):
  randomint = random.randint(1,6)
  monster_name = monster.get('name')
  if monster.get('strength') > randomint:
    print(f'You were defeated by {monster_name}')
  else:
    print(f'You defeated {monster_name}')

def pickup(character, trophy):
  print('You found something!')