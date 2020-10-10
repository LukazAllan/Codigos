from random import randint as rd
from time import sleep as dly
from json import load
import logging, emoji
#from matplotlib import pyplot as plt
#import numpy as np

#plt.style.use('fivethirtyeight')
#x = np.arange(3)
#larg = 0.25
#y = [[],[]]

with open("compeca.log", "w", encoding="UTF-8") as f:
    f.write('cheguei\n')
    pass
def info(msg):
    with open("compeca.log", "a", encoding="UTF-8") as f:
        f.write(f'{msg}\n')
        pass
logging.basicConfig(filename="competir.log", filemode="w", level = logging.DEBUG)
logger = logging.getLogger()
logger.info('cheguei')

A0Z25 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z','AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL',
         'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AY', 'AZ','BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL',
         'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BY', 'BZ']
data = []
with open('jogadores.json', encoding='UTF-8') as f:
    p = load(f)
ganhadores=[]
for partida in range(1):
    #y[0].append(0)
    #y[1].append(0)
    for x in range(1):
        a = p.copy()
        # por exemplo, 32 part., dividir em grupos c 4 integrantes
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

        #Apresentção
        for c in data:
            dly(1.25)
            print(f'Grupo {A0Z25[cont]}:')
            for b in range(len(c)):
                dly(0.5)
                print(f'{b+1}.{c[b][0]}')
            cont += 1
            print('')


        pto= lambda x: x[1]
        input()

        for a in range(len(data)):
            camp = data[a].copy()
            print(f'Disputas Grupo {A0Z25[a]}')
            info(f"Grupo {A0Z25[a]}")
            for c in range(len(camp)):
                op = camp[c+1:len(camp)].copy()
                for b in range(len(op)):
                    res = [0, 0]
                    print(f'{camp[c][0]} vs. {op[b][0]}')
                    while res[0] == res[1]:
                        res = [rd(0, 100), rd(0, 100)]
                    #dly(1.5)
                    if res[0] > res[1]:
                        camp[c][1] += 1
                        print(emoji.emojize(f' {camp[c][0]} vence! \n'))
                    else:
                        camp[c+b+1][1] += 1
                        print(emoji.emojize(f' {camp[c+b+1][0]} vence! \n'))
                    #dly(1)
            camp.sort(key=pto, reverse=True)
            data[a] = camp.copy()
            for c in range(len(camp)):
                print(f'{c+1}. {camp[c][0]}  {camp[c][1]}')
            print('')
            #dly(1)
            pontos = []
            for c in camp:
                pontos.append(c[1])
            if pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
                desempate = 0
                while pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
                    desempate += 1
                    if pontos.count(1) == 3 and len(pontos) != 3:
                        logger.info("if pontos.count(1) == 3 and len(pontos) != 3:")
                        camp = data[a][1:].copy()
                    elif pontos.count(2) == 3 and len(pontos) != 3:
                        logger.info("elif pontos.count(2) == 3 and len(pontos) != 3:")
                        camp = data[a][:3].copy()
                    elif pontos.count(2) == 2 and pontos[0] == 3:
                        logger.info("elif pontos.count(2) == 2 and pontos[0] == 3:")
                        camp = data[a][1:3].copy()
                    for x in range(len(camp)):
                        camp[x][1] = 0
                    print(f'Desempate {desempate} Grupo {A0Z25[a]}')
                    info(f'Desempate {desempate}')
                    logger.info(f"{camp} - 1")
                    for c in range(len(camp)):
                        op = camp[c+1:len(camp)].copy()
                        for b in range(len(op)):
                            res = [0, 0]
                            print(emoji.emojize(f'{camp[c][0]} vs. {op[b][0]}'))
                            while res[0] == res[1]:
                                res = [rd(0, 100), rd(0, 100)]
                                if res[0] == res[1]:
                                    print("Empate! Jogando de novo!")
                                    dly(3)
                            #dly(3)
                            if res[0] > res[1]:
                                camp[c][1] += 1
                                print(emoji.emojize(f'{camp[c][0]} vence!\n'))
                            else:
                                camp[c+b+1][1] += 1
                                print(emoji.emojize(f'{camp[c+b+1][0]} vence!\n'))
                            #dly(1)
                    camp.sort(key=pto, reverse=True)
                    logger.info(f"{camp} - 2")
                    print(f'Desempate {desempate} Grupo {A0Z25[a]}')
                    for c in range(len(camp)):
                        print(f'{c+2}. {camp[c][0]}  {camp[c][1]}')
                    print('')
                    pontos = []
                    if pontos.count(1) == 3 and len(pontos) != 3:
                        logger.info("if pontos.count(1) == 3 and len(pontos) != 3:")
                        #camp = data[a][1:].copy()
                        for c in range(len(camp)):
                            data[c+1] = camp[c]
                    elif pontos.count(2) == 3 and len(pontos) != 3:
                        logger.info("elif pontos.count(2) == 3 and len(pontos) != 3:")
                        # camp = data[a][:3].copy()
                        for c in range(len(camp)):
                            data[c] = camp[c]
                    elif pontos.count(2) == 2 and pontos[0] == 3:
                        logger.info("elif pontos.count(2) == 2 and pontos[0] == 3:")
                        # camp = data[a][1:3].copy()
                        for c in range(len(camp)):
                            data[c+1] = camp[c]
                    #dly(1)
            else:
                info("Passou direto, sem empates")
                pass
            #dly(1)
        for x in range(len(data)):
            data[x].sort(key=pto, reverse=True)
        
        print("Para a próxima fase: ")
        for c in range(len(data)):
            dly(1)
            print(emoji.emojize(f' :crown: Grupo {A0Z25[c]} :crown:'))
            for b in range(2):
                dly(1.5)
                print(emoji.emojize(f'{b+1}° {data[c][b][0]}'))
            print('')

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
                print('Semi Final')
                pass
            elif len(data) == 1:
                pass
                print('Final')
            else:
                print(f'{len(data)}ᵃ de Final')
                pass
            for c in range(len(data)):
                dly(1)
                print(emoji.emojize(f'{c+1}°Jogo: {data[c][0][0]} vs. {data[c][1][0]}'))
                print('')
            # apresentação
            for a in range(len(data)):
                camp = data[a].copy()
                for c in range(len(camp)):
                    op = camp[c+1:len(camp)].copy()
                    for b in range(len(op)):
                        res = [0, 0]
                        print(f'{camp[c][0]} vs. {op[b][0]}')
                        while res[0] == res[1]:
                            res = [rd(0, 200), rd(0, 200)]
                            if res[0] == res[1]:
                                print("Empate! Jogando de novo!")
                                dly(3)
                        dly(1.5)
                        if res[0] > res[1]:
                            camp[c][1] += 1
                            print(f'{camp[c][0]} vence!\n')
                        else:
                            camp[c+b+1][1] += 1
                            print(f'{camp[c+b+1][0]} vence!\n')
                        dly(1)
                camp.sort(key=pto, reverse=True)
                data[a] = camp.copy()
                print('')
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
        print(emoji.emojize(f'Ganhador: :crown:{data[0][0][0]}:crown: Parabéns!'))
        ganhadores.append(data[0][0][0])
        if data[0][0][2] == 'M':
            pass
            #y[0][partida] += 1
        elif data[0][0][2] == 'F':
            pass
            #y[1][partida] += 1

    #plt.bar(partida - larg, y[0][partida], width=larg, color='#2300dd')
    #plt.bar(partida, y[1][partida], width=larg, color='#e502bd')
#print(ganhadores)
#plt.show()
