import os.path as path, urllib.request as req, emoji
from canivete import rinput
from json import load
from conf import jogo, tit, cls, acc, Print, abre
def init():
    query1 = rinput('Jogo: Novo / Carregar ', ['n', 'c'], '>>')
    data_cont = list()
    if query1 == 'n':
        """
        jog = [['Allan'],['Luan']]"""
        jog = [[input('Jogador 1, qual o teu nome?').strip()],[input('Jogador 2, qual o teu nome?').strip()]]
        slot = False
        print(f"{tit('Database')}\nJá existe um arquivo disponível no disco")
        for c in range(2):
            print(f"usá-lo, Descarregar do repositório ou Carregar outro?")
            i = rinput('>>', ['u', 'c', 'd'], '')
            if 'u' in i.lower():
                data_cont.append(abre())
            elif 'c' in i.lower():
                print('Qual o nome do arquivo?(Sem extensão)\nLembre de verificar se o arquivo\nestá na mesma pasta deste código.')
                while True:
                    arquivo = input('>> ').strip()
                    if path.isfile(f'{arquivo}.csv') == True:
                        data_cont.append(abre(arquivo))
                        break
            elif 'd' in i.lower():
                req.urlretrieve('https://drive.google.com/uc?authuser=0&id=1v-BbhiTD_1pATcrLNttVK0C_akUVnl-l&export=download', 'data1.csv')
                data_cont.append(abre())
            if c == 0:
                stay = rinput('Usar um slot para cada um?\n[s/n] ', ['s', 'n'], '>>')
                if 'n' in stay.lower():
                    break
                if 's' in stay.lower():
                    slot = True
                    pass

        imp = ''
        #print(f'{data_cont}\n')
        if not slot:
            for a in range(-1, len(data_cont[0])):
                if a == -1:
                    try:
                        print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
                    except UnicodeEncodeError:
                        print(f" *|Nv|{'Nome' :>17}|\033[31mPV\033[m|\033[31mPA\033[m|\033[32mS\033[m|")
                else:
                    print(f"{(a + 1) :>2}|{data_cont[0][a]['nivel']:>2}|{data_cont[0][a]['nome']:>17}|{data_cont[0][a]['pvt'] :>2}|{data_cont[0][a]['pa']:>2}|{data_cont[0][a]['s']}|{(data_cont[0][a]['pv'] + data_cont[0][a]['s'] + data_cont[0][a]['pa'])}")
            for a in range(1, 3):
                while True:
                    if a == 1:
                        imp = input(f'{jog[0][0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
                    elif a == 2:
                        imp = input(f'{jog[1][0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
                    esc = imp.strip().split(',')
                    n = False
                    if imp == '':
                        break
                    for c in range(0, len(esc)):
                        #print(f"For {c} in range, and len(data_cont[0]) == {len(data_cont[0])}")
                        if esc[c].isnumeric() == True:
                            esc[c]: int = int(esc[c])
                            if esc[c] <= len(data_cont[0]):
                                if c == len(esc) - 1:
                                    n = True
                                    #print(n)
                                pass
                            else:
                                break
                        else:
                            break
                    if n == True:
                        if a == 1:
                            print(esc)
                            if len(esc) == 1 and esc[0] == 0:
                                # print('estou dentro')
                                for a in range(0, len(data_cont[0])):
                                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                                    jog[0].append(data_cont[0][a].copy())
                            elif len(esc) != 1 and esc[0] == 0:
                                for a in range(0, len(data_cont[0])):
                                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                                    jog[0].append(data_cont[0][a].copy())
                                for c in range(1, len(esc)):
                                    jog[0].append(data_cont[0][(esc[c] - 1)].copy())
                            else:
                                # print('considerei diferente de zero')
                                for c in esc:
                                    jog[0].append(data_cont[0][c - 1].copy())
                        elif a == 2:
                            print(esc)
                            if len(esc) == 1 and esc[0] == 0:
                                print('estou dentro')
                                for a in range(0, len(data_cont[0])):
                                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                                    jog[1].append(data_cont[0][a].copy())
                            elif len(esc) != 1 and esc[0] == 0:
                                for a in range(0, len(data_cont[0])):
                                    # print('passei pelo for in range pela {}° vez.' .format(a+1))
                                    jog[1].append(data_cont[0][a].copy())
                                for c in range(0, len(esc)):
                                    jog[1].append(data_cont[0][(esc[c] - 1)].copy())
                            else:
                                # print('considerei else')
                                for c in esc:
                                    jog[1].append(data_cont[0][c - 1].copy())
                        break
                    if n == False:
                        pass
        else:
            for a in range(-1, len(data_cont[0])):
                if a == -1:
                    print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
                else:
                    print(f"{(a + 1) :>2}|{data_cont[0][a]['nivel']:>2}|{data_cont[0][a]['nome']:>17}|{data_cont[0][a]['pvt'] :>2}|{data_cont[0][a]['pa']:>2}|{data_cont[0][a]['s']}|{(data_cont[0][a]['pv'] + data_cont[0][a]['s'] + data_cont[0][a]['pa'])}")
            while True:
                imp = input(f'{jog[0][0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
                esc = imp.strip().split(',')
                n = False
                if imp == '':
                    break
                for c in range(0, len(esc)):
                    #print(f"For {c} in range, and len(data_cont[0]) == {len(data_cont[0])}")
                    if esc[c].isnumeric() == True:
                        esc[c]: int = int(esc[c])
                        if esc[c] <= len(data_cont[0]):
                            if c == len(esc) - 1:
                                n = True
                                #print(n)
                            pass
                        else:
                            break
                    else:
                        break
                if n == True:
                    print(esc)
                    if len(esc) == 1 and esc[0] == 0:
                        # print('estou dentro')
                        for a in range(0, len(data_cont[0])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            jog[0].append(data_cont[0][a].copy())
                    elif len(esc) != 1 and esc[0] == 0:
                        for a in range(0, len(data_cont[0])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            jog[0].append(data_cont[0][a].copy())
                        for c in range(1, len(esc)):
                            jog[0].append(data_cont[0][(esc[c] - 1)].copy())
                    else:
                        # print('considerei diferente de zero')
                        for c in esc:
                            jog[0].append(data_cont[0][c - 1].copy())
                    break
                if n == False:
                    pass
            for a in range(-1, len(data_cont[1])):
                if a == -1:
                    print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
                else:
                    print(f"{(a + 1) :>2}|{data_cont[1][a]['nivel']:>2}|{data_cont[1][a]['nome']:>17}|{data_cont[1][a]['pvt'] :>2}|{data_cont[1][a]['pa']:>2}|{data_cont[1][a]['s']}|{(data_cont[1][a]['pv'] + data_cont[1][a]['s'] + data_cont[1][a]['pa'])}")
            while True:
                imp = input(f'{jog[0][0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
                esc = imp.strip().split(',')
                n = False
                if imp == '':
                    break
                for c in range(0, len(esc)):
                    #print(f"For {c} in range, and len(data_cont[1]) == {len(data_cont[1])}")
                    if esc[c].isnumeric() == True:
                        esc[c]: int = int(esc[c])
                        if esc[c] <= len(data_cont[1]):
                            if c == len(esc) - 1:
                                n = True
                                #print(n)
                            pass
                        else:
                            break
                    else:
                        break
                if n == True:
                    print(esc)
                    if len(esc) == 1 and esc[0] == 0:
                        # print('estou dentro')
                        for a in range(0, len(data_cont[1])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            jog[1].append(data_cont[1][a].copy())
                    elif len(esc) != 1 and esc[0] == 0:
                        for a in range(0, len(data_cont[1])):
                            # print('passei pelo for in range pela {}° vez.' .format(a+1))
                            jog[1].append(data_cont[1][a].copy())
                        for c in range(1, len(esc)):
                            jog[1].append(data_cont[1][(esc[c] - 1)].copy())
                    else:
                        # print('considerei diferente de zero')
                        for c in esc:
                            jog[1].append(data_cont[1][c - 1].copy())
                    break
                if n == False:
                    pass
        for c in range(1, len(jog[0])):
            print(f"{c}. {jog[0][c]['nome']}")
        conf = [[int(input(f'{jog[0][0]}, escolha teu capitão '))]]
        for c in range(1, len(jog[1])):
            print(f"{c}. {jog[1][c]['nome']}")
        conf[0].append(int(input(f'{jog[1][0]}, escolha teu capitão ')))

    elif query1 == 'c':
        file = open('salve.json', encoding='utf-8')
        cr = load(file)
        jog[0] = [list(cr.keys())[0]]
        jog[1] = [list(cr.keys())[1]]
        conf = [list(cr.values())[2]]
        for c in list(cr.values())[0]:
            jog[0].append(c)
        for c in list(cr.values())[1]:
            jog[1].append(c)
    jogo(jog[0], jog[1], conf[0])