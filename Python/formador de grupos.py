from random import randint as rd
from time import sleep as dly

A0Z25=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']

div=[]
p=[['Allan',0], ['Bruno',0], ['Carlos',0], ['Diego',0],
    ['Elton',0], ['Fabiano',0], ['Nicolas',0], ['Miguel',0],
    ['Vitor',0], ['Pedro',0], ['Gustavo',0], ['Guilherme',0],
    ['Eduardo',0], ['Thiago',0], ['Rodrigo',0], ['Igor',0],
    ['Júlio',0], ['Heitor',0], ['Luiz',0], ['Rafael',0],
    ['Davi',0],['Luan',0], ['Yuri',0],['Paulo',0],
   ['Henrique',0], ['Eduardo',0], ['Daniel',0], ['Caio',0],
   ['Lucas',0], ['Alec',0], ['Enzo',0], ['Jânio',0]]
a = p.copy()
#por exemplo, 31 part., dividir em grupos c 4 integrantes
integrantes =4
total=len(a)#32
grupos=len(a)//integrantes
for grupo in range(grupos):#4 = grupos
    g=[]
    for c in range(integrantes):#4 = integrantes nos grupos
        if not len(a) == 0:
            al = rd(0, len(a)-1)
        else:
            al=0
        g.append(a[al])
        a.remove(a[al])
    div.append(g)
    
if len(a) != 0:
    div.append(a)
    a = []
'''
método qdo div com grupos divididos
for jog in a:
    for cont in range(100):
        g = rd(0,len(div)-1)
        #g = int(input(f'{jog} vai pra: '))-1
        if len(div[g]) == 8:
            pass
                
        else:
            div[g].append(jog)
            break
          
'''  
cont = 0
for c in div:
    dly(1)
    print(f'Grupo {A0Z25[cont]}:')
    for b in range(len(c)):
        dly(2)
        print(f'{b+1}.{c[b][0]}')
    cont += 1
    print('')
