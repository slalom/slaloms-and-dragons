from item import Item
import random

names = ['Sword','Axe','Dagger','Wand','Bow','Shield']
qualities = ['Common','Uncommon','Rare','Epic','Legendary']

def generate_random_item():
    name = random.choice(names)
    quality = random.choice(qualities)
    # item_type = "Weapon"
    if name == 'Shield':
        item_type = 'Armor'
    else:
        item_type = 'Weapon'

    if name == 'Shield':
        modifier = "+5 to Constitution"
    else:
        modifier = "+5 to Strength"    

    item = Item(name, quality, item_type, modifier)
    return item

# Tests

item_1 = generate_random_item()
item_2 = generate_random_item()
item_3 = generate_random_item()

print(item_1.name)
print(item_2.name)
print(item_3.name)

print(item_1.item_type)
print(item_2.item_type)
print(item_3.item_type)
