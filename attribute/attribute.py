level = 0
exp = 0
level_dict = {}


# Attributes description
class Attribute ():
    def __init__(self, level, exp, level_dict):
        self.level = 0  # level
        self.exp = 0   # exp
        # level dict maps levels with history of actions
        # level_dict = {0: ['list of history'], 1: }
        self.level_dict = {}
        # abilities
        self.abilities = []


def make_attribute(attribute):
    attribute = Attribute(level, exp, level_dict)
    return attribute
