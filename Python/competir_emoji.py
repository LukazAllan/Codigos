from random import randint as rd
from time import sleep as dly
from json import load
from competir_def import *
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
with open('jgadores.json', encoding='UTF-8') as f:
    p = load(f)
ganhadores=[]
min_range = 0
max_range = min_range + 10

data = fase_class_elim(p.copy())
cont = 0

show(data)

pto = lambda x: x[1]
input()

data = tatakau(data, False)

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
    show(data)
    # apresentação
    for a in range(len(data)):
        camp = data[a].copy()
        for c in range(len(camp)):
            op = camp[c+1:len(camp)].copy()
            for b in range(len(op)):
                res = [0, 0]
                print(f'{camp[c][0]} vs. {op[b][0]}')
                while res[0] == res[1]:
                    res = [rd(min_range, max_range), rd(min_range, max_range)]
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
