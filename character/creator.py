import character.Character

def new():
  print("Select your character!")
  return character.Character.Character({'name': 'Guido', 'race': 'Halfling', 'gender':'male', 'strength':4, 'dexterity': 5, 'constitution': 3, 'hitpoints': 9})
