import random

# Dictionary with powers and descriptions
powers = {
    "Sword": "Heimdall let me borrow his Sword",
    "Knife": "I have lots of sharp knives",
    "Flight": "Ever Seen Neo Fly. Yeah I can do that",
    "ExtraStrength": "Think Hulk stength but no gamma radiation",
    "Invisibility": "I’ve mastered the ability of standing so incredibly still that I become invisible to the eye. Watch. My movement’s so slow that it’s imperceptible."}

# Special powers
special_power = {
    1: "Ability to read minds",
    2: "Ability to talk to Dragons",
    3: "I have ultra instinct level perception"}


class power():
    def GetPower(self):
        power = list(powers)[random.randint(0, len(powers) - 1)]
        specialPower = special_power[list(
            special_power)[random.randint(0, len(special_power) - 1)]]
        return (power, specialPower)
