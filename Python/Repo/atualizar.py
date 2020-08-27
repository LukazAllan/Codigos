#ver 1.0.5
import csv
from random import randint as rand
while True:
    far = input('Nome do arquivo sem a extensão\n>> ')
    ar = open(f'{far}.csv', encoding='utf-8')
    read = csv.reader(ar, delimiter=',')
    data = {
        'temp': [],
        'lixo': []
    }
    for r in read:
        #linha [Nv, Nome, Hp, atk, luck]
        try:
            lin = [int(r[0]), r[1], int(r[2]), int(r[3]), int(r[4]) ]
            data['temp'].append(lin)
        except IndexError:
            pass
    print('CSV Controller ver. 1')
    while True:
        while True:
            com = input('>> ').split(' ')
            if com[0] == 'add':
                linha = [2, input('Digite o nome: ').strip(), rand(10, 20), rand(10, 20), rand(2, 11)]
                data['temp'].append(linha)
            elif com[0] == 'rem':
                if not com[1].isnumeric() and com[1] == 'rev':
                    try:
                        if com[2]:
                            data['temp'].append(data['lixo'][int(com[2])-1])
                            data['lixo'].pop(int(com[2])-1)
                    except IndexError:
                        pass
                else:
                    data['lixo'].append(data['temp'][int(com[1])-1])
                    data['temp'].pop(int(com[1])-1)
            elif com[0] == 'ajuste':
                for p in range(0, len(data['temp'])):
                    lvl = (data['temp'][p][2]+data['temp'][p][3]+data['temp'][p][4])//5
                    data['temp'][p][0] = lvl
            elif com[0] == 'lixo':
                for c in range(0, len(data['lixo'])):
                    print(f"{c+1}. Nv. {data['lixo'][c][0]} {data['lixo'][c][1]:>17}, hp: {data['lixo'][c][2]:>3}, atq: {data['lixo'][c][3]:>2},  luck: {data['lixo'][c][4]:>2}")
            elif com[0] == 'list':
                for c in range(0, len(data['temp'])):
                    print(f"{c+1}. Nv. {data['temp'][c][0]} {data['temp'][c][1]:>17}, hp: {data['temp'][c][2]:>3}, atq: {data['temp'][c][3]:>2},  luck: {data['temp'][c][4]:>2}")
            elif com[0] == 'help' or com[0] == 'ajuda':
                try:
                    if com[1]:
                        if com[1] == 'add':
                            print('add:\n    Adiciona mais um integrante aos dados')
                        elif com[1] == 'rem':
                            print('rem:\n    Remove o integrante escolhido dos dados.')
                        elif com[1] == 'lixo':
                            print('lixo:\n    Exibe a lista dos integrantes removidos\n    nesta sessão')
                        elif com[1] == 'lista':
                            print('list:\n    Lista os integrantes no arquivo')
                        elif com[1] == 'upg':
                            print('upg:\n    Evolue integrantes deste arquivo\n    funções:\n        upg ou upg *\n            evolue todos da lista\n        upg [num]\n            evolue um integrante da lista')
                except IndexError:
                    print('Comandos: add, rem, lixo, list, upg, ajuste\npara mais info, digite: ajuda [comando]')
            elif com[0] == 'upg':
                try:
                    com[1] = com[1].split(',')
                    for c in range(0, len(com[1])):
                        com[1][c] = int(com[1][c]) -1
                    for p in com[1]:
                        linha = data['temp'][p]
                        at = [rand(2, 5), rand(2, 5), rand(2, 5)]
                        at.append(at[0]+at[1]+ at[2])
                        if at[3] == 15:
                            print ('Evolução topzera')
                        elif 12 <= at[3] < 15:
                            print ('Evolução prata')
                        elif 10 <= at[3] < 12:
                            print ('Evolução bronze')
                        elif 8 <= at[3] < 10:
                            print ('Evolução normal')
                        linha[2] += at[0]
                        linha[3] += at[1]
                        linha[4] += at[2]
                        linha[0] = (linha[2]+linha[3]+linha[3])//5
                except IndexError and ValueError:
                    for p in range(0, len(data['temp'])):
                        linha = data['temp'][p]
                        at = [rand(2, 5), rand(2, 5), rand(2, 5)]
                        at.append(at[0]+at[1]+ at[2])
                        if at[3] == 15:
                            print ('Evolução topzera')
                        elif 12 <= at[3] < 15:
                            print ('Evolução prata')
                        elif 10 <= at[3] < 12:
                            print ('Evolução bronze')
                        elif 8 <= at[3] < 10:
                            print ('Evolução normal')
                        linha[2] += at[0]
                        linha[3] += at[1]
                        linha[4] += at[2]
                        linha[0] = (linha[2]+linha[3]+linha[3])//5
            elif com[0] == 'sair':
                break
            elif com[0] == 'salvar':
                with open(f'{far}.csv', 'w') as arquivo:
                    csv_writer = csv.writer(arquivo, delimiter=',')
                    for es in range(0, len(data['temp'])):
                        #linha [Nv, Nome, Hp, atk, luck]
                        csv_writer.writerow(data['temp'][es])
                ar.close()
                break
        per = input('Continuar editando? ')
        if per == 'n':
            break
    per = input('Sair? ')
    if per == 's':
        break
