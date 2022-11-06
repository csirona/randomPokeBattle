from battle.battle import setup

def run():
    print('Welcome to RandomBattles')
    ntrainer=input("What's your name of Pokemon's Trainer?: ")
    
    rivals=setup(ntrainer)
    print('your oponent is '+rivals[1].name.__str__() )

    print('Wich Pokemon use?: ')

if __name__== '__main__':
    run()