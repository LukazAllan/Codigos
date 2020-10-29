from random import randint as rd
from time import sleep as dly
import emoji

min_range = 0
max_range = min_range + 10
pto = lambda x: x[1]


A0Z25 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z','AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL',
         'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AY', 'AZ','BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL',
         'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BY', 'BZ']


def fase_class_elim(lista:list):
    result = []
    integrantes = 4
    total = len(lista)  # 32
    grupos = total//integrantes
    for grupo in range(grupos):  # 4 = grupos
        g = []
        for c in range(integrantes):  # 4 = integrantes nos grupos
            if not len(lista) == 0:
                al = rd(0, len(lista)-1)
            else:
                al = 0
            g.append(lista[al])
            lista.remove(lista[al])
        result.append(g)

    if len(lista) != 0:
        result.append(a)
        a = []
    return result


def show(data:list):
    """
    param data: lista que contém grupos
    """
    #Apresentação
    first = len(data[0])
    if first != 2:
        cont = 0
        for c in data:
            dly(1.25)
            print(f'Grupo {A0Z25[cont]}:')
            for b in range(len(c)):
                dly(0.5)
                print(f'{b+1}.{c[b][0]}')
            cont += 1
            print('')
    else:
        if len(data) == 2:
            print('Semi Final')
            pass
        elif len(data) == 1:
            print('Final')
            pass
        else:
            print(f'{len(data)}ᵃ de Final')
            pass
        for c in range(len(data)):
            dly(1)
            print(f'{c+1}°Jogo: {data[c][0][0]} vs. {data[c][1][0]}')
            print('')


def tatakau(data:list, assistido:bool=True):
    for a in range(len(data)):
        camp = data[a].copy()
        print(f'Disputas Grupo {A0Z25[a]}' if assistido else '')
        #info(f"Grupo {A0Z25[a]}")
        for c in range(len(camp)):
            op = camp[c+1:len(camp)].copy()
            for b in range(len(op)):
                res = [0, 0]
                print(f'{camp[c][0]} vs. {op[b][0]}' if assistido else '')
                while res[0] == res[1]:
                    res = [rd(min_range, max_range), rd(min_range, max_range)]
                if assistido:
                    dly(1.5)
                if res[0] > res[1]:
                    camp[c][1] += 1
                    print(emoji.emojize(f' {camp[c][0]} vence! \n') if assistido else '')
                else:
                    camp[c+b+1][1] += 1
                    if assistido:
                        print(emoji.emojize(f' {camp[c+b+1][0]} vence! \n') if assistido else '')
                if assistido:
                    dly(1)
        camp.sort(key=pto, reverse=True)
        data[a] = camp.copy()
        if assistido:
            for c in range(len(camp)):
                print(f'{c+1}. {camp[c][0]}  {camp[c][1]}')
            print('')
            dly(1)
        pontos = []
        for c in camp:
            pontos.append(c[1])
        if pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
            desempate = 0
            while pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
                desempate += 1
                if pontos.count(1) == 3 and len(pontos) != 3:
                    #logger.info("if pontos.count(1) == 3 and len(pontos) != 3:")
                    camp = data[a][1:].copy()
                elif pontos.count(2) == 3 and len(pontos) != 3:
                    #logger.info("elif pontos.count(2) == 3 and len(pontos) != 3:")
                    camp = data[a][:3].copy()
                elif pontos.count(2) == 2 and pontos[0] == 3:
                    #logger.info("elif pontos.count(2) == 2 and pontos[0] == 3:")
                    camp = data[a][1:3].copy()
                for x in range(len(camp)):
                    camp[x][1] = 0
                print(f'Desempate {desempate} Grupo {A0Z25[a]}' if assistido else '')
                #info(f'Desempate {desempate}')
                #logger.info(f"{camp} - 1")
                for c in range(len(camp)):
                    op = camp[c+1:len(camp)].copy()
                    for b in range(len(op)):
                        res = [0, 0]
                        print(emoji.emojize(f'{camp[c][0]} vs. {op[b][0]}') if assistido else '')
                        while res[0] == res[1]:
                            res = [rd(min_range, max_range), rd(min_range, max_range)]
                            if res[0] == res[1]:
                                if assistido:
                                    print("Empate! Jogando de novo!")
                                    dly(3)
                        if assistido:
                            dly(3)
                        if res[0] > res[1]:
                            camp[c][1] += 1
                            print(emoji.emojize(f'{camp[c][0]} vence!\n') if assistido else '')
                        else:
                            camp[c+b+1][1] += 1
                            print(emoji.emojize(f'{camp[c+b+1][0]} vence!\n') if assistido else '')
                        if assistido:
                            dly(1)
                camp.sort(key=pto, reverse=True)
                #logger.info(f"{camp} - 2")
                if assistido:
                    print(f'Desempate {desempate} Grupo {A0Z25[a]}')
                    for c in range(len(camp)):
                        print(f'{c+2}. {camp[c][0]}  {camp[c][1]}')
                    print('')
                pontos = []
                if pontos.count(1) == 3 and len(pontos) != 3:
                    #logger.info("if pontos.count(1) == 3 and len(pontos) != 3:")
                    #camp = data[a][1:].copy()
                    for c in range(len(camp)):
                        data[c+1] = camp[c]
                elif pontos.count(2) == 3 and len(pontos) != 3:
                    #logger.info("elif pontos.count(2) == 3 and len(pontos) != 3:")
                    # camp = data[a][:3].copy()
                    for c in range(len(camp)):
                        data[c] = camp[c]
                elif pontos.count(2) == 2 and pontos[0] == 3:
                    #logger.info("elif pontos.count(2) == 2 and pontos[0] == 3:")
                    # camp = data[a][1:3].copy()
                    for c in range(len(camp)):
                        data[c+1] = camp[c]
                if assistido:
                    dly(1)
        else:
            #info("Passou direto, sem empates")
            pass
        if assistido:
            dly(1)
    return data