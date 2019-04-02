import game.tools as tools


class npc:

    def __init__(self, name, npc_class, greeting):
        self.name = name
        self.npc_class = npc_class
        self.greeting = greeting

    def meet(self):
        print(self.greeting)
        answer = tools.show_picker(['YES', 'NO'])
        if answer == 'YES':
            print('Wonderful!')
        else:
            print('whatevs.')
