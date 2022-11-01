class  Trainer():
    
    def __init__(self, name,poke1,poke2,poke3,poke4):
        self.name = name
        self.poke1=poke1
        self.poke2=poke2
        self.poke3=poke3
        self.poke4=poke4
        
    def __str__(self):
        return self.name