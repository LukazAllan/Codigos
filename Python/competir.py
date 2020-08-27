from random import randint as rd
from time import sleep as dly
from matplotlib import pyplot as plt
import numpy as np

#plt.style.use('fivethirtyeight')
x = np.arange(3)
larg = 0.25
y = [[],[]]


A0Z25 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
data = []
p = [['Allan', 0, 'M'], ['Bruno', 0, 'M'], ['Carlos', 0, 'M'], ['Diego', 0, 'M'],
     ['Elton', 0, 'M'], ['Fabiano', 0, 'M'], ['Nicolas', 0, 'M'], ['Miguel', 0, 'M'],
     ['Vitor', 0, 'M'], ['Pedro', 0, 'M'], ['Gustavo', 0, 'M'], ['Guilherme', 0, 'M'],
     ['Eduardo', 0, 'M'], ['Thiago', 0, 'M'], ['Rodrigo', 0, 'M'], ['Igor', 0, 'M'],
     ['Júlio', 0, 'M'], ['Heitor', 0, 'M'], ['Luiz', 0, 'M'], ['Rafael', 0, 'M'],
     ['Davi', 0, 'M'], ['Luan', 0, 'M'], ['Yuri', 0, 'M'], ['Paulo', 0, 'M'],
     ['Henrique', 0, 'M'], ['Celso', 0, 'M'], ['Daniel', 0, 'M'], ['Caio', 0, 'M'],
     ['Lucas', 0, 'M'], ['Alec', 0, 'M'], ['Enzo', 0, 'M'], ['Jânio', 0, 'M'],

     ['Maria', 0, 'F'], ['Leila', 0, 'F'], ['Rafaela', 0, 'F'], ['Julia', 0, 'F'],
     ['Evelyn', 0, 'F'], ['Giovanna', 0, 'F'], ['Sarah', 0, 'F'], ['Amanda', 0, 'F'],
     ['Sofia', 0, 'F'], ['Ágatha', 0, 'F'], ['Luiza', 0, 'F'], ['Manuela', 0, 'F'],
     ['Gabrielle', 0, 'F'], ['Raissa', 0, 'F'], ['Brenda', 0, 'F'], ['Marina', 0, 'F'],
     ['Eduarda', 0, 'F'], ['Isabella', 0, 'F'], ['Lina', 0, 'F'], ['Aline', 0, 'F'],
     ['Clara', 0, 'F'], ['Larissa', 0, 'F'], ['Beatriz', 0, 'F'], ['Anna', 0, 'F'],
     ['Letícia', 0, 'F'], ['Vitória', 0, 'F'], ['Marina', 0, 'F'], ['Luciana', 0, 'F'],
     ['Caroline', 0, 'F'], ['Lívia', 0, 'F'], ['Júlia', 0, 'F'], ['Camila', 0, 'F']
     ]
ganhadores=[]
for partida in range(25):
    y[0].append(0)
    y[1].append(0)
    for x in range(10):
        a = p.copy()
        # por exemplo, 64 part., dividir em grupos c 4 integrantes
        integrantes = 4
        total = len(a)  # 32
        grupos = len(a)//integrantes
        for grupo in range(grupos):  # 4 = grupos
            g = []
            for c in range(integrantes):  # 4 = integrantes nos grupos
                if not len(a) == 0:
                    al = rd(0, len(a)-1)
                else:
                    al = 0
                g.append(a[al])
                a.remove(a[al])
            data.append(g)

        if len(a) != 0:
            data.append(a)
            a = []
        cont = 0
        # for c in data:
            #dly(1.25)
            #print(f'Grupo {A0Z25[cont]}:')
            # for b in range(len(c)):
                #dly(0.5)
                #print(f'{b+1}.{c[b][0]}')
            # cont += 1
            #print('')


        def pto(ponto): return ponto[1]


        for a in range(len(data)):
            camp = data[a].copy()
            #print(f'Disputas Grupo {A0Z25[a]}')
            for c in range(len(camp)):
                op = camp[c+1:len(camp)].copy()
                for b in range(len(op)):
                    res = [0, 0]
                    #print(f'{camp[c][0]} vs. {op[b][0]}')
                    while res[0] == res[1]:
                        res = [rd(0, 100), rd(0, 100)]
                    #dly(1.5)
                    if res[0] > res[1]:
                        camp[c][1] += 1
                        #print(f'{camp[c][0]} vence!\n')
                    else:
                        camp[c+b+1][1] += 1
                        #print(f'{camp[c+b+1][0]} vence!\n')
                    #dly(1)
            camp.sort(key=pto, reverse=True)
            data[a] = camp.copy()
            # for c in range(len(camp)):
                #print(f'{c+1}. {camp[c][0]}  {camp[c][1]}')
            #print('')
            #dly(1)
            pontos = []
            for c in camp:
                pontos.append(c[1])
            if pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
                desempate = 1
                while pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
                    desempate += 1
                    if pontos.count(1) == 3 and len(pontos) != 3:
                        camp = data[a][1:].copy()
                    elif pontos.count(2) == 3 and len(pontos) != 3:
                        camp = data[a][:3].copy()
                    elif pontos.count(2) == 2 and pontos[0] == 3:
                        camp = data[a][1:3].copy()
                    for x in range(len(camp)):
                        camp[x][1] = 0
                    #print(f'Desempate {desempate} Grupo {A0Z25[a]}')
                    for c in range(len(camp)):
                        op = camp[c+1:len(camp)].copy()
                        for b in range(len(op)):
                            res = [0, 0]
                            #print(f'{camp[c][0]} vs. {op[b][0]}')
                            while res[0] == res[1]:
                                res = [rd(0, 100), rd(0, 100)]
                            #dly(3)
                            if res[0] > res[1]:
                                camp[c][1] += 1
                                #print(f'{camp[c][0]} vence!\n')
                            else:
                                camp[c+b+1][1] += 1
                                #print(f'{camp[c+b+1][0]} vence!\n')
                            #dly(1)
                    camp.sort(key=pto, reverse=True)
                    #print(f'Desempate {desempate} Grupo {A0Z25[a]}')
                    # for c in range(len(camp)):
                        #print(f'{c+2}. {camp[c][0]}  {camp[c][1]}')
                    #print('')
                    pontos = []
                    for c in camp:
                        pontos.append(c[1])
                    if pontos.count(1) != 3:
                        data[a][1][1] += 1
                    else:
                        pass
                    #dly(1)
            else:
                pass
            #dly(1)
        for x in range(len(data)):
            data[x].sort(key=pto, reverse=True)
        # for c in range(len(data)):
            #dly(1)
            #print(f'Vencedores Grupo {A0Z25[c]}')
            # for b in range(2):
                #dly(1.5)
                #print(f'{b+1}. {data[c][b][0]} {data[c][b][1]}')
            #print('')

        metdogp = int((len(data)/2))
        for c in range(len(data)):
            data[c] = data[c][:2]
        qrdd = []
        for x in range(int((len(data)/2))):
            qrdd.append([[data[x][1][0], 0, data[x][1][2]], [data[metdogp+x][0][0], 0, data[metdogp+x][0][2]]])
            qrdd.append([[data[x][0][0], 0, data[x][0][2]], [data[metdogp+x][1][0], 0, data[metdogp+x][1][2]]])
        data = qrdd.copy()
        while True:
            if len(data) == 2:
                #print('Semi Final')
                pass
            elif len(data) == 1:
                pass
                #print('Final')
            else:
                #print(f'{len(data)}ᵃ de Final')
                pass
            # for c in range(len(data)):
                #dly(1)
                #print(f'{c+1}°Jogo: {data[c][0][0]} vs. {data[c][1][0]}')
                #print('')
            # apresentação
            for a in range(len(data)):
                camp = data[a].copy()
                for c in range(len(camp)):
                    op = camp[c+1:len(camp)].copy()
                    for b in range(len(op)):
                        res = [0, 0]
                        #print(f'{camp[c][0]} vs. {op[b][0]}')
                        while res[0] == res[1]:
                            res = [rd(0, 100), rd(0, 100)]
                        #dly(1.5)
                        if res[0] > res[1]:
                            camp[c][1] += 1
                            #print(f'{camp[c][0]} vence!\n')
                        else:
                            camp[c+b+1][1] += 1
                            #print(f'{camp[c+b+1][0]} vence!\n')
                        #dly(1)
                camp.sort(key=pto, reverse=True)
                data[a] = camp.copy()
                #print('')
            # jogos
            if len(data) == 1:
                break
            metdogp = int((len(data)/2))
            for c in range(len(data)):
                data[c].sort(key=pto, reverse=True)
                data[c] = data[c][:1]
            qrdd = []
            for x in range(int((len(data)/2))):
                qrdd.append([[data[x][0][0], 0, data[x][0][2]], [data[metdogp+x][0][0], 0, data[metdogp+x][0][2]]])
            data = qrdd.copy()
        data[0].sort(key=pto, reverse=True)
        #print(f'Ganhador: {data[0][0][0]} Parabéns!')
        ganhadores.append(data[0][0][0])
        if data[0][0][2] == 'M':
            y[0][partida] += 1
        elif data[0][0][2] == 'F':
            y[1][partida] += 1

    plt.bar(partida - larg, y[0][partida], width=larg, color='#2300dd')
    plt.bar(partida, y[1][partida], width=larg, color='#e502bd')
print(ganhadores)
plt.show()
