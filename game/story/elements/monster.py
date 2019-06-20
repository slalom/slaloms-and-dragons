import random


def build():
    return {
        "type": "monster",
        "monster": {"name": random.choice(__names), "strength": random.randint(1, 10)},
        "view": "👾",
    }


__names = [
    "Gremlin",
    "Davy Jones",
    "Chupacabra",
    "Manticore",
    "Banshee",
    "Poltergeist",
    "Nessie",
    "Revenant",
    "The Jersey devil",
    "Headless Horseman",
    "Zombie",
    "Yeti",
    "Drop bear",
    "Mummy",
    "Orc",
    "Kraken",
    "Golem",
    "Werewolf",
    "Godzilla",
    "Cerberus",
    "Siren",
    "Succubus",
    "Incubus",
    "Cyclops",
    "Sasquatch",
    "Nandi bear",
    "Rakshasa",
    "Basilisk",
    "Changeling",
    "Frankenstein",
    "Vampire",
    "Snallygaster",
    "Windigo",
    "Penanggalan",
    "Ogbanje",
    "Glawackus",
]
