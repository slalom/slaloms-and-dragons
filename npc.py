
class Npc: 
    """
    creates a class of non-player characters 

    """ 
    def __init__(self, name, npc_class, greeting): 
        self.name = name 
        self.npc_class = npc_class 
        self.greeting = greeting 

    def meet(self): 
        print(self.greeting)



