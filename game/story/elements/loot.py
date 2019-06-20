import random


def build():
    return {
        "type": "loot",
        "loot": {"name": random.choice(__names), "value": random.randint(1, 10)},
        "view": "💰",
    }


__names = [
    "The Sword of Damocles",
    "Dragon Scales",
    "Invisibility Cloak",
    "Gold Doubloons",
    "Chain Mail",
    "Iron Mace",
]
