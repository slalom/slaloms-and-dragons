import game.character.character as character

def new():
  print("Select your character!")
  hero = character.Character({'name': 'Guido',
                                        'race': 'Halfling', 
                                        'gender':'male', 
                                        'strength':4, 
                                        'dexterity': 5, 
                                        'constitution': 3, 
                                        'hitpoints': 9})

  print(f'Welcome {hero.name}!')

  return hero
