#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:58:03 2019

@author: rickk
"""

#test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20}


class Character:
    def __init__(self, character):
        self.name = character["name"]
        self.race = character["race"]
        self.gender = character["gender"]
        self.strength = character["strength"]
        self.dexterity = character["dexterity"]
        self.constitution = character["constitution"]
        self.hitpoints = character["hitpoints"]

#character = Character(test_character)
#print("Character Name:", character.name)
#print("Character race:", character.race)
