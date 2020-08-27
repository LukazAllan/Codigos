from time import sleep as slp
from random import choice as ch
from matplotlib import pyplot as plt
import numpy as np


class Pers:
    pass

class Fire:

    def __init__(self, hp, name):
        self.name = name
        self.hp = hp
        self.type = Fire

    def atq(self, who):
        if self.hp > 0:
            who.hp -= 3
            if type(who) == Plant:
                who.hp -= 1

class Water:

    def __init__(self, hp, name):
        self.name = name
        self.hp = hp
        self.type = Water

    def atq(self, who):
        if self.hp > 0:
            who.hp -= 3
            if type(who) == Fire:
                who.hp -= 1

class Plant:

    def __init__(self, hp, name):
        self.name = name
        self.hp = hp
        self.type = Plant

    def atq(self, who):
        if self.hp > 0:
            who.hp -= 3
            if type(who) == Water:
                who.hp -= 1


a = Fire(20, 'charmander')
b = Plant(20, 'bulbasaur')
c = Water(20, 'squirtle')
#print(a.hp, b.hp)
x = [a.name, b.name, c.name]
y = [0,0,0]
plt.style.use('fivethirtyeight')
for p in range(10):
    for x in range(50):
        while True:
            at = ch([a,b,c])
            if at == a:
                df = ch([b,c])
                at.atq(df)
                #print(f'{a.name} ataca {df.name}!!!')
            elif at == b:
                df = ch([a,c])
                at.atq(df)
                #print(f'{at.name} ataca {df.name}!!!')
            else:
                df = ch([a,b])
                at.atq(df)
                #print(f'{at.name} ataca {df.name}!!!')
            if a.hp < 0:
                a.hp = 0
            elif c.hp < 0:
                c.hp = 0
            elif b.hp < 0:
                b.hp = 0
            #slp(2)
            #print(f'{a.name}: {a.hp} {b.name}: {b.hp} {c.name}: {c.hp}')
            if a.hp == 0 and b.hp == 0:
                y[2] += 1
                #print('c vence')
                break
            elif c.hp == 0 and a.hp == 0:
                y[1] += 1
                #print('b vence')
                break
            elif b.hp == 0 and c.hp == 0:
                y[0] += 1
                #print('a vence')
                break
            #slp(2)
        a.hp = 20
        b.hp = 20
        c.hp = 20
    # gráficos
    x = np.arange(3)
    larg = 0.25
    plt.bar(p - larg,y[0], width=larg, color='#f91f1f')
    plt.bar(p,y[1], width=larg, color='#0EA353')
    plt.bar(p + larg,y[2], width=larg, color='#9ED3F3')
    for td in range(len(y)):
        y[td]=0
plt.title('Desempenho por categoria')
plt.xlabel('classes')
plt.ylabel('Partidas Ganhas')
plt.show()
#b.atq(a)
#print(a.__dict__)
