import random
import requests
import json
import time
from pokemon.pokemon import Pokemon
from trainer.trainer import Trainer

inicio = time.time()
#function to initialize pokemons of a trainer
def setPoke():
    url = "https://pokeapi.co/api/v2/pokemon/"
    num = random.randint(252,386)
    strNum = str(num)


    response = requests.get(url+strNum)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        namePoke= data['name']
        lenMove = len(data['moves'])
        moves = ['','','','']
        for i in range(4):
            ranMov=random.randint(0,lenMove-1)
            mov= data['moves'][ranMov]['move']['name']
            moves[i]=mov
        hp = data['stats'][0]['base_stat']
        att = data['stats'][1]['base_stat']
        defen = data['stats'][2]['base_stat']
        spAtt = data['stats'][3]['base_stat']
        spDef= data['stats'][4]['base_stat']
        speed = data['stats'][5]['base_stat']
        p1=Pokemon(namePoke,3,hp,moves[0],moves[1],moves[2],moves[3],att,defen,spAtt,spDef,speed)
        return p1
        

poke1=setPoke()

print(poke1.name+str(poke1.ps)+ ' '+poke1.move1+ ' '+poke1.move2+ ' '+poke1.move3+ ' '+poke1.move4)


#function to set pokemons to a trainer
def setTrainer(trainerName: str, poke1:Pokemon,poke2:Pokemon,poke3:Pokemon,poke4:Pokemon):
    trainer=Trainer(trainerName,poke1,poke2,poke3,poke4)
    
    print(trainer.poke1.__str__())



#Damage formula-> (PS) = {([{(2 * Nv. / 5 + 2) * Ataque * Poder / Defensa} / 50] * 1°Mod. + 2) * STAB * Efec.Tipo#1 * Efec.Tipo#2 * 2°Mod. * Rnd / 100} * CH;
def Damage(poke:Pokemon):
    nv=poke.level

    
 
    

fin = time.time()
print(fin-inicio) 