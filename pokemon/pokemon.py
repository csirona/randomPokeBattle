
# Create class pokemon with its atributes
class Pokemon():
    
    def __init__(self,name,level,ps,move1,move2,move3,move4,defense,attack,spAttack,spDefense,speed):
        self.name = name
        self.level = level
        self.ps = ps
        self.move1 = move1
        self.move2 = move2
        self.move3 =  move3
        self.move4 = move4
        self.attack =attack
        self.defense = defense
        self.spAttack =spAttack
        self.spDefense = spDefense
        self.speed = speed

        
    def __str__(self):
        return self.name
    
    def damage(self,dam):
        self.ps = self.ps - dam
        print( self.ps+" PS")

    #method to know if a pokemon is still alive        
    def isAlive(self):
        if self.ps <=0:
            print("Pokemon is dead")
        
        
