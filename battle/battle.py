import random
import requests
import json
import time
from move.move import Move
from pokemon.pokemon import Pokemon
from trainer.trainer import Trainer

inicio = time.time()
#function to initialize pokemons with their features
def setPoke():
    url = "https://pokeapi.co/api/v2/pokemon/"
    movUrl="https://pokeapi.co/api/v2/move/"
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
        
        move_to_poke=['','','','','','','','','','','','']
        for i in range(4):
            ranMov=random.randint(0,lenMove-1)
            mov= data['moves'][ranMov]['move']['name']
            moves[i]=mov
            
            res = requests.get(movUrl+moves[i])
            if res.status_code != 200: 
                #response could be too extensive
                #print(response.text)
                print("not 200 status")
               
            else:
                #json the data, then save in a array to put in the array move_to_poke
                moveData=res.json()
                mtp=['','','']
                mtp[0]=moveData['name']
                mtp[1]=moveData['type']['name']
                mtp[2]=moveData['power']
                move_to_poke[i]=mtp
                
                
        
        mov1=Move(move_to_poke[0][0],move_to_poke[0][1],move_to_poke[0][2])
        mov2=Move(move_to_poke[1][0],move_to_poke[1][1],move_to_poke[1][2])
        mov3=Move(move_to_poke[2][0],move_to_poke[2][1],move_to_poke[2][2])
        mov4=Move(move_to_poke[3][0],move_to_poke[3][1],move_to_poke[3][2])
                
        hp = data['stats'][0]['base_stat']
        att = data['stats'][1]['base_stat']
        defen = data['stats'][2]['base_stat']
        spAtt = data['stats'][3]['base_stat']
        spDef= data['stats'][4]['base_stat']
        speed = data['stats'][5]['base_stat']
        p1=Pokemon(namePoke,3,hp,mov1,mov2,mov3,mov4,att,defen,spAtt,spDef,speed)
        return p1
        


#Damage formula-> (PS) = {([{(2 * Nv. / 5 + 2) * Ataque * Poder / Defensa} / 50] * 1°Mod. + 2) * STAB * Efec.Tipo#1 * Efec.Tipo#2 * 2°Mod. * Rnd / 100} * CH;
#incomplete... trying to avoid modificators
def damage(poke:Pokemon, garyPoke:Pokemon, move:Move):
    nv=poke.level
    dam= (((2*nv/5+2)*poke.attack*move.power/poke.defense)/50)
    print('ps gary '+str(garyPoke.ps))
    print(str(dam))

#show your moves and ask wich one you want to use
def battle(myPoke:Pokemon, garyPoke: Pokemon):
    print(myPoke.name +' can use: ')
    time.sleep(1)
    mv=input('[1] '+myPoke.move1.name+ ' - '+'[2] '+myPoke.move2.name+ ' - '+'[3] '+myPoke.move3.name+ ' - '+'[4] '+myPoke.move4.name+ ' - ')
    if mv == '1':
        move = myPoke.move1
    elif mv == '2':
        move = myPoke.move2
    elif mv == '3':
        move = myPoke.move3
    elif mv == '4':
        move = myPoke.move4
    else:
        print('Invalid value')
    damage(myPoke, garyPoke,move)
    print(garyPoke.name+' PSs is '+str(garyPoke.ps))
    
#set names, pokemons and moves     
def setup(ntrainer):
    
    #Set up oponent
    op_poke1 = setPoke()
    op_poke2 = setPoke()
    op_poke3 = setPoke()
    op_poke4 = setPoke()
    
    op=Trainer('Gary',op_poke1,op_poke2,op_poke3,op_poke4)
    poke1=setPoke()
    poke2=setPoke()
    poke3=setPoke()
    poke4=setPoke()
    u=Trainer(ntrainer,poke1,poke2,poke3,poke4)

    return [u,op]
    
#ask if you  want attack or use a object (item)
def action(u,op):   
    choosen_poke=input('[1] '+u.poke1.name+'  [2] '+u.poke2.name+'  [3] '+u.poke3.name+'  [4] '+u.poke4.name)
    if choosen_poke == '1':
        print('Is your turn '+u.poke1.name)
        print('What do you want to do?: ')
        first_choose=input('[ 1 ] Attack! - [ 2 ] Item ')
        time.sleep(1)
        if first_choose =='1':
            battle(u.poke1, op.poke1)
    elif choosen_poke=='2':
        print('Is your turn '+u.poke2.name)
        print('What do you want to do?: ')
        first_choose=input('[ 1 ] Attack! - [ 2 ] Item ')
        if first_choose =='1':
            battle(u.poke2, op.poke1)
    elif choosen_poke=='3':
        print('Is your turn '+u.poke3.name)
        print('What do you want to do?: ')
        first_choose=input('[ 1 ] Attack! - [ 2 ] Item ')
        if first_choose =='1':
            battle(u.poke3, op.poke1)         
    elif choosen_poke=='4':
        print('Is your turn '+u.poke4.name)
        print('What do you want to do?: ')
        first_choose=input('[ 1 ] Attack! - [ 2 ] Item ')
        if first_choose =='1':
            battle(u.poke4, op.poke1)
    else:
        print('Invalid Option')
   

fin = time.time()
print(fin-inicio) 



