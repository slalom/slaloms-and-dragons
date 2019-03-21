import random

def fight(character, monster):
  hero_score = character.strength + random.randint(1,6)
  monster_score = monster['strength'] + random.randint(1,6)
  monster_name = monster['name']
  
  if hero_score > monster_score:
    print(f'You defeated {monster_name}')
  else:
    print(f'You were defeated by {monster_name}')

def pickup(character, trophy):
  print('You found something!')
