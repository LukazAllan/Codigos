import csv, random
from os import path, system
from typing import List
from json import dump
from time import localtime as lct


def abre(path='data2'):
    with open(f'{path}.csv', encoding='utf-8') as csvfile:
        data1 = list()
        data = csv.reader(csvfile, delimiter=',')
        #print(data)
        #cls()
        cont: int = -1
        for row in data:
            cont += 1
            try:
                data1.append({'nivel' : int(row[0]), 'nome' : row[1], 'pv' : int(row[2]), 'pvt' : int(row[2]), 'pa' : int(row[3]), 's' : int(row[4])})
            except IndexError:
                pass
    return data1


def tit(txt):
    t = int(len(txt) + 8)
    print('-' * t)
    print(f'{txt:^{t}}')
    print('-' * t)


def cls():
    android: bool = path.exists('/storage/emulated/0')
    windows: bool = path.exists('C:/Program Files')
    linux: bool = path.exists('/home/')
    if android or linux:
        system('clear')
    if windows:
        system('cls')


def acc(J1, J2):
    pa1 = int(0)
    pv1 = int(0)
    ps1 = int(0)
    pa2 = int(0)
    pv2 = int(0)
    ps2 = int(0)
    for c in range(1, len(J1)):
        if J1[c]['pv'] != 0:
            pv1 = pv1 + int(J1[c]['pv'])
            pa1 = pa1 + int(J1[c]['pa'])
            ps1 = ps1 + int(J1[c]['s'])
        else:
            pass
    for c in range(1, len(J2)):
        if J2[c]['pv'] != 0:
            pv2 = pv2 + int(J2[c]['pv'])
            pa2 = pa2 + int(J2[c]['pa'])
            ps2 = ps2 + int(J2[c]['s'])
        else:
            pass
    ac1 = ((pa1+pv1+ps1)/(pa1+pv1+ps1+pa2+pv2+ps2)*100)
    ac2 = ((pa2+pv2+ps2)/(pa1+pv1+ps1+pa2+pv2+ps2)*100)
    return (ac1, ac2)


def Print(J1, J2):
    a = acc(J1, J2)
    if a[0] >= 60 and a[1] <= 40:
        if a[0] != 100:
            if a[0] <= 90:
                print(f"\033[7;32m{'Ganhando':>17} {a[0] :.2f}%\033[m{' ' * 7}\033[7;31m{a[1] :.2f}%{' ' * 18}\033[m")
                print(f"\033[7;32m{J1[0]:>24}\033[m{' ' * 7}\033[7;31m{J2[0]:<24}\033[m")
            else:
                print(f"\033[7;32m{'Ganhando':>17} {a[0] :.2f}%\033[m{' ' * 7}\033[7;31m{a[1] :.2f}%{' ' * 19}\033[m")
                print(f"\033[7;32m{J1[0]:>24}\033[m{' ' * 7}\033[7;31m{J2[0]:<24}\033[m")
        else:
            print(f"\033[7;32m{'Ganhou':>16} {a[0] :.2f}%\033[m{' ' * 7}\033[7;31m{a[1] :.2f}%{' ' * 19}\033[m")
            print(f"\033[7;32m{J1[0]:>24}\033[m{' ' * 7}\033[7;31m{J2[0]:<24}\033[m")
    elif a[0] <= 40 and a[1] >= 60:
        if a[1] != 100:
            print(f"\033[7;31m{a[0] :>23.2f}%\033[m{' ' * 7}\033[7;32m{a[1] :<4.2f}% Ganhando{' ' * 9}\033[m")
            print(f"\033[7;31m{J1[0]:>24}\033[m{' ' * 7}\033[7;32m{J2[0]:<24}\033[m")
        else:
            print(f"\033[7;31m{a[0] :>23.2f}%\033[m{' ' * 7}\033[7;32m{a[1] :<4.2f}% Ganhou{' ' * 10}\033[m")
            print(f"\033[7;31m{J1[0]:>24}\033[m{' ' * 7}\033[7;32m{J2[0]:<24}\033[m")
    else:
        print(f"{a[0] :>24.2f}%{' ' * 7}{a[1] :.2f}%")
        print(f"{J1[0]:>24}{' ' * 7}{J2[0]}")
    if len(J1) == len(J2):
        for c in range(1, len(J1)):
            if J1[c]['pv'] > (2 * J1[c]['pvt'] / 3):
                print(f"\033[7;32m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            elif (J1[c]['pvt'] / 3) < J1[c]['pv'] <= (2 * J1[c]['pvt'] / 3):
                print(f"\033[7;33m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            elif 0 < J1[c]['pv'] <= (J1[c]['pvt'] / 3):
                print(f"\033[7;31m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            elif J1[c]['pv'] == 0:
                print(f"\033[7;30m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
            if J2[c]['pv'] > (2 * J2[c]['pvt'] / 3):
                print(f"\033[7;32m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            elif (J2[c]['pvt'] / 3) < J2[c]['pv'] <= (2 * J2[c]['pvt'] / 3):
                print(f"\033[7;33m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            elif 0 < J2[c]['pv'] <= (J2[c]['pvt'] / 3):
                print(f"\033[7;31m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            elif J2[c]['pv'] == 0:
                print(f"\033[7;30m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")

    elif len(J1) != len(J2):
        if len(J1) > len(J2):
            for c in range(1, len(J2)):
                if J1[c]['pv'] > (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;32m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif (J1[c]['pvt'] / 3) < J1[c]['pv'] <= (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;33m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif 0 < J1[c]['pv'] <= (J1[c]['pvt'] / 3):
                    print(f"\033[7;31m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif J1[c]['pv'] == 0:
                    print(f"\033[7;30m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                if J2[c]['pv'] > (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;32m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif (J2[c]['pvt'] / 3) < J2[c]['pv'] <= (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;33m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif 0 < J2[c]['pv'] <= (J2[c]['pvt'] / 3):
                    print(f"\033[7;31m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif J2[c]['pv'] == 0:
                    print(f"\033[7;30m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            for a in range(len(J2), len(J1)):
                if J1[a]['pv'] > (2 * J1[a]['pvt'] / 3):
                    print(f"\033[7;32m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
                elif (J1[a]['pvt'] / 3) < J1[a]['pv'] <= (2 * J1[a]['pvt'] / 3):
                    print(f"\033[7;33m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
                elif 0 < J1[a]['pv'] <= (J1[a]['pvt'] / 3):
                    print(f"\033[7;31m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
                elif J1[a]['pv'] == 0:
                    print(f"\033[7;30m{J1[a]['nome'] :>17} {J1[a]['pa']:>2} {J1[a]['pv'] :>3}\033[m  {a :>2}   ")
        elif len(J1) < len(J2):
            for c in range(1, len(J1)):
                if J1[c]['pv'] > (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;32m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif (J1[c]['pvt'] / 3) < J1[c]['pv'] <= (2 * J1[c]['pvt'] / 3):
                    print(f"\033[7;33m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif 0 < J1[c]['pv'] <= (J1[c]['pvt'] / 3):
                    print(f"\033[7;31m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                elif J1[c]['pv'] == 0:
                    print(f"\033[7;30m{J1[c]['nome'] :>17} {J1[c]['pa']:>2} {J1[c]['pv'] :>3}\033[m  {c :>2}   ", end='')
                if J2[c]['pv'] > (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;32m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif (J2[c]['pvt'] / 3) < J2[c]['pv'] <= (2 * J2[c]['pvt'] / 3):
                    print(f"\033[7;33m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif 0 < J2[c]['pv'] <= (J2[c]['pvt'] / 3):
                    print(f"\033[7;31m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
                elif J2[c]['pv'] == 0:
                    print(f"\033[7;30m{J2[c]['pv'] :<3} {J2[c]['pa']:>2} {J2[c]['nome'] :<17}\033[m")
            for a in range(len(J1), len(J2)):
                if J2[a]['pv'] > (2 * J2[a]['pvt'] / 3):
                    print(f"{'' :>26}{a :>2}   \033[7;32m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
                elif (J2[a]['pvt'] / 3) < J2[a]['pv'] <= (2 * J2[a]['pvt'] / 3):
                    print(f"{'' :>26}{a :>2}   \033[7;33m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
                elif 0 < J2[a]['pv'] <= (J2[a]['pvt'] / 3):
                    print(f"{'' :>26}{a :>2}   \033[7;31m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")
                elif J2[a]['pv'] == 0:
                    print(f"{'' :>26}{a :>2}   \033[7;30m{J2[a]['pv'] :<3} {J2[a]['pa']:>2} {J2[a]['nome'] :<17}\033[m")


def jogo(J1 = list(), J2 = list(), sel = list(), caminho = f'{lct()[0]}-{lct()[1]:0>2}-{lct()[2]:0>2}-{lct()[3]:0>2}-{lct()[4]:0>2}-{lct()[5]:0>2}'):
    """

    :type J1: object
    """
    sel.insert(0,'nulo')
    print(sel)
    while True:
        arq = open(f'{caminho}.json', 'w', encoding='utf-8')
        dump({J1[0]: J1[1:len(J1)], J2[0]: J2[1:len(J2)], "sel": sel[1:]}, arq, ensure_ascii=False)
        arq.close()
        sorte = [False, False, False, False, False, False, False, False, False, False, False, False]
        Print(J1, J2)
        b = acc(J1,J2)
        if int(b[0]) == 100:
            print(f"{J1[0]} Ganhou!!")
            break
        elif int(b[1]) == 100:
            print(f"{J2[0]} Ganhou!!")
            break
        com: List[str] = input('>> ').split(' ')
        """if com[0] != 'sel' or com[0] != 'sub' or com[0] != 'atq' or com[0] != 'sudo' or com[0] != 'ajuda' or com[0] != 'help' or com[0] != 'sair':
            while True:
                com: List[str] = input('>> ').split(' ')
                if com[0] == 'sel' or com[0] == 'sub' or com[0] == 'atq' or com[0] == 'sudo' or com[0] == 'ajuda' or com[0] == 'help' or com[0] == 'sair':
                    break"""
        if com[0] == 'sel' and len(com) == 3:
            if com[1].isnumeric() and com[2].isnumeric():
                # sel 1 1
                com[2]: int = int(com[2])
                com[1]: int = int(com[1])
                sel.insert(1, com[1])
                sel.insert(2, com[2])
                while True:
                    com: List[str] = input('>> ').split(' ')
                    if com[0] == 'sel' and len(com) == 3:
                        if com[1].isnumeric() and com[2].isnumeric():
                            # sel 1 1
                            com[2]: int = int(com[2])
                            com[1]: int = int(com[1])
                            sel.insert(1, com[1])
                            sel.insert(2, com[2])
                    elif com[0] == 'sub' and len(com) == 3:
                        if com[2].isnumeric() == True:
                            com[2]: int = int(com[2])
                            if com[1] == 'j1':
                                sel.pop(1)
                                sel.insert(1, com[2])
                            elif com[1] == 'j2':
                                sel.pop()
                                sel.insert(2, com[2])
                    elif com[0] != 'sub' and com[0] != 'sel':
                        break
        if com[0] == 'sub':
            while True:
                try:
                    if com[2].isnumeric() == True:
                        break
                except IndexError:
                    print('Digite quem você quer trocar.')
                    com: List[str] = input('>> ').split(' ')
            if sel != ['nulo']:
                com[2]: int = int(com[2])
                if com[1] == 'j1':
                    sel.pop(1)
                    sel.insert(1, com[2])
                elif com[1] == 'j2':
                    sel.pop()
                    sel.insert(2, com[2])
                while com[0] == 'sel' or com[0] == 'sub':
                    com: List[str] = input('>> ').split(' ')
                    if com[0] == 'sel' and com[1].isnumeric() and com[2].isnumeric():
                        # sel 1 1
                        com[2]: int = int(com[2])
                        com[1]: int = int(com[1])
                        sel.insert(1, com[1])
                        sel.insert(2, com[2])
                        com: List[str] = input('>> ').split(' ')
                    if com[0] == 'sub' and com[2].isnumeric() == True:
                        com[2]: int = int(com[2])
                        if com[1] == 'j1':
                            sel.pop(1)
                            sel.insert(1, com[2])
                        elif com[1] == 'j2':
                            sel.pop()
                            sel.insert(2, com[2])
                else:
                    pass
            else:
                print('Selecione primeiro, antes de substituí-lo\ncomando: sel (Jogador 1) (Jogador 2)')
        if 'atq' == com[0]:
            try:
                if com[1] == 'j1':
                    if J1[sel[1]]['pv'] != 0:
                        #print('estou dentro')
                        for c in range(0, (J1[sel[1]]['s'] + 1)):
                            sorte.insert(0, True)
                        rad: int = random.randint(1, (len(sorte) - 1))
                        atdf: bool = sorte[rad]
                        print(rad, atdf)
                        if atdf:
                            print(f"{J2[sel[2]]['nome']} defendeu-se.")
                        else:
                            if J2[sel[2]]['pv'] - J1[sel[1]]['pa'] >= 0:
                                # print('considerei if')
                                J2[sel[2]]['pv'] -= J1[sel[1]]['pa']
                            else:
                                # print('considerei else')
                                J2[sel[2]]['pv'] = 0
                                pass
                        if J2[sel[2]]['pv'] == 0:
                             pass
                    else:
                        print(f'{J1[sel[1]]["nome"]} tem 0 de vida, não pode atacar')
                    sorte = [False, False, False, False, False, False, False, False, False, False, False, False]
                    if J2[sel[2]]['pv'] != 0:
                        # print('estou dentro')
                        for c in range(0, (J1[sel[1]]['s'] + 1)):
                            sorte.insert(0, True)
                        rad: int = random.randint(1, (len(sorte) - 1))
                        atdf: bool = sorte[rad]
                        print(rad, atdf)
                        if atdf:
                            print(f"{J1[sel[1]]['nome']} defendeu-se")
                        else:
                            if J1[sel[1]]['pv'] - J2[sel[2]]['pa'] >= 0:
                                #print('considerei if')
                                J1[sel[1]]['pv'] -= J2[sel[2]]['pa']
                            else:
                                #print('considerei else')
                                J1[sel[1]]['pv'] = 0
                                pass
                        if J1[sel[1]]['pv'] == 0:
                            pass
                    else:
                        print(f'{J2[sel[2]]["nome"]} tem 0 de vida, não pode atacar')
                elif com[1] == 'j2':
                    if J2[sel[2]]['pv'] != 0:
                        # print('estou dentro')
                        for c in range(0, (J1[sel[1]]['s'] + 1)):
                            sorte.insert(0, True)
                        rad: int = random.randint(1, (len(sorte) - 1))
                        atdf: bool = sorte[rad]
                        print(rad, atdf)
                        if atdf:
                            print(f"{J1[sel[1]]['nome']} defendeu-se")
                        elif atdf == False and J1[sel[1]]['pv'] != 0:
                            if J1[sel[1]]['pv'] - J2[sel[2]]['pa'] >= 0:
                                #print('considerei if')
                                J1[sel[1]]['pv'] -= J2[sel[2]]['pa']
                            else:
                                #print('considerei else')
                                J1[sel[1]]['pv'] = 0
                                pass
                        elif atdf == False and J1[sel[1]]['pv'] == 0:
                            pass
                    else:
                        print(f'{J2[sel[2]]["nome"]} tem 0 de vida, não pode atacar')
                    sorte = [False, False, False, False, False, False, False, False, False, False, False, False]
                    if J1[sel[1]]['pv'] != 0:
                        #print('estou dentro')
                        for c in range(0, (J1[sel[1]]['s'] + 1)):
                            sorte.insert(0, True)
                        rad: int = random.randint(1, (len(sorte) - 1))
                        atdf: bool = sorte[rad]
                        print(rad, atdf)
                        if atdf:
                            print(f"{J2[sel[2]]['nome']} defendeu-se.")
                        elif atdf == False and J2[sel[2]]['pv'] != 0:
                            if J2[sel[2]]['pv'] - J1[sel[1]]['pa'] >= 0:
                                # print('considerei if')
                                J2[sel[2]]['pv'] -= J1[sel[1]]['pa']
                            else:
                                # print('considerei else')
                                J2[sel[2]]['pv'] = 0
                                pass
                        elif atdf == False and J2[sel[2]]['pv'] == 0:
                             pass
                    else:
                        print(f'{J1[sel[1]]["nome"]} tem 0 de vida, não pode atacar')
            except IndexError:
                print('Ou você ainda não selecionou os personagens, ou você esqueceu que tem que especificar quem ataca\ncomando: sel (Jogador 1) (Jogador 2)')
        if com[0] == 'sair':
            break
        if com[0] == 'sudo':
            if com[1] == 'hp':
                if com[2] == 'j1' and bool(com[3]) == True and bool(com[4]) == True:
                    # sudo hp j1 1 100
                    com[4]: int = int(com[4])
                    com[3]: int = int(com[3])
                    J1[com[3]]['pv'] += com[4]
                if com[2] == 'j2' and bool(com[3]) == True and bool(com[4]) == True:
                    # sudo hp j2 1 100
                    com[4]: int = int(com[4])
                    com[3]: int = int(com[3])
                    J2[com[3]]['pv'] += com[4]
            elif com[1] == 'atq':
                try:
                    if com[2] == 'j1' and bool(com[3]) and bool(com[4]) and bool(com[5]):
                        # sudo atq j1 100 1 1
                        com[4]: int = int(com[4])
                        com[5]: int = int(com[5])
                        if J2[com[5]]['pv'] != 0:
                            com[3]: int = int(com[3])
                            if J2[com[5]]['pv'] - J1[com[4]]['pa'] >= 0:
                                # print('considerei if')
                                J2[com[5]]['pv'] -= com[3]
                            else:
                                J2[com[5]]['pv'] = 0
                                pass
                        else:
                            pass
                    if com[2] == 'j2' and bool(com[3]) and bool(com[4]) and bool(com[5]):
                        # sudo atq j2 100 1 1
                        com[4]: int = int(com[4])
                        com[5]: int = int(com[5])
                        if J1[sel[2]]['pv'] != 0:
                            com[3]: int = int(com[3])
                            if J1[com[5]]['pv'] - J2[com[4]]['pa'] >= 0:
                                # print('considerei if')
                                J1[com[5]]['pv'] -= com[3]
                            else:
                                J1[com[5]]['pv'] = 0
                                pass
                        else:
                            pass
                except IndexError:
                    try:
                        if com[2] == 'j1' and bool(com[3]):
                            # sudo atq j1 100
                            if J2[sel[2]]['pv'] != 0:
                                com[3]: int = int(com[3])
                                if J2[sel[2]]['pv'] - J1[sel[1]]['pa'] >= 0:
                                    #print('considerei if')
                                    J2[sel[2]]['pv'] -= com[3]
                                else:
                                    J2[sel[2]]['pv'] = 0
                                    pass
                            else:
                                pass
                        if com[2] == 'j2' and bool(com[3]):
                            # sudo atq j2 100
                            if J1[sel[1]]['pv'] != 0:
                                com[3]: int = int(com[3])
                                if J1[sel[1]]['pv'] - J2[sel[2]]['pa'] >= 0:
                                    J1[sel[1]]['pv'] -= com[3]
                                else:
                                    J1[sel[1]]['pv'] = 0
                                    pass
                            else:
                                pass
                    except IndexError:
                        print('Você ainda não selecionou os personagens\ncomando: sel (Jogador 1) (Jogador 2)')
        if com[0] == 'help' or com[0] == 'ajuda':
            print('Comandos:\nPara mais detalhes, digite: ajuda [comando]\nsel - selecionar/sub - substituir\natq - ataque / sair - sai da partida')
