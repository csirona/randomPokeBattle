class Move():
    
    def __init__(self,name,type,power):
        self.name = name
        self.type = type
        self.power = power
        
    def __str__(self):
        return self.name