#test_character = {"name":"Slalom", "race":"Elf", "gender":"female", "strength":10, "dexterity":10, "constitution":10, "hitpoints":20, "inventory": [], "level":0, "experience":560}


class Character:
    def __init__(self, character):
        '''
        character: dictionary passed from create_character function
        '''
        self.name = character["name"]
        self.race = character["race"]
        self.gender = character["gender"]
        self.strength = character["strength"]
        self.dexterity = character["dexterity"]
        self.constitution = character["constitution"]
        self.hitpoints = character["hitpoints"]
        self.inventory = character["inventory"]
        self.experience = character["experience"]
        self.level = character["level"]

    def print_character(self, window):
        window.addstr(f'Name: {self.name}\n')
        window.addstr(f'Race: {self.race} \n')
        window.addstr(f'Gender: {self.gender} \n')
        window.addstr(f'Strength: {self.strength} \n')
        window.addstr(f'Dexterity: {self.dexterity} \n')
        window.addstr(f'Constitution: {self.constitution} \n')
        window.addstr(f'Hitpoints: {self.hitpoints} \n')
        window.addstr(f'Inventory: {self.inventory} \n')
        window.addstr(f'Experience: {self.experience} \n')
        window.addstr(f'Level: {self.level} \n')

    def calc_level(self):
        calc_level = self.experience // 100
        if calc_level > self.level:
            #self.level_up()
            pass
        self.level = calc_level

    def pickup(self, item):
        if item["name"] not in self.inventory: 
            self.inventory.append(item["name"])
            return '' 
        else: 
            return f'\n... Unfortunately you already have {item["name"]}.'

    def take_damage(self, damage):
        self.hitpoints -= damage

    def die(self):
        self.hitpoints = 0

    def is_alive(self):
        return self.hitpoints > 0

    def __str__(self):
        string = "Class: Character\nCharacter Name: " + self.name
        return string
