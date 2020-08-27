import os.path as path, urllib.request as req, emoji, logging
from canivete import rinput
from conf import jogo, tit, cls, acc, Print, abre
logging.basicConfig(filename='camp.log', filemode='w', format='%(asctime)s %(levelname)s - %(message)s',level=logging.DEBUG)
log = logging.getLogger()
def init():
    armaz = list()
    query1 = rinput('Jogo: Novo / Carregar ', ['n', 'c'], '>>')
    config = []
    config.append(int(rinput('Quantos jogadores haverão para esse campeonato?', ['4','8','16'], errormsg='A resposta tem que ser um número quadrado perfeito superior a 2')))
    config.append(int(rinput('Quantos personagens haverão por jogador?', errormsg='A resposta tem que ser um número')))
    log.debug(f'\n     config: {config}')
    jog = []
    for c in range(config[0]):
        jog.append([input(f'Jogador {c+1}, qual o teu nome?').strip()])
    log.debug(f'\n     jog: {jog}')
    print(f"{tit('Database')}\nJá existe um arquivo disponível no disco")
    for c in range(config[0]):
        print(f"Usá-lo, Descarregar do repositório ou Carregar outro?")
        i = rinput('>>', ['u', 'c', 'd'], '')
        if 'u' in i:
            armaz.append(abre())
        elif 'c' in i:
            print('Qual o nome do arquivo?(Sem extensão)\nLembre de verificar se o arquivo\nestá na mesma pasta deste código.')
            while True:
                arquivo = input('>> ').strip()
                if path.isfile(f'{arquivo}.csv') == True:
                    armaz.append(abre(arquivo))
                    break
                else:
                    log.error('caminho não encontrado')
        elif 'd' in i:
            req.urlretrieve('https://drive.google.com/uc?authuser=0&id=1v-BbhiTD_1pATcrLNttVK0C_akUVnl-l&export=download', 'data1.csv')
            armaz.append(abre())
    log.debug(f'\n     armaz: {armaz}')
    for b in range(len(armaz)):
        print(emoji.emojize(f" *|Nv|{'Nome' :>17}|\033[31m:heart:\033[m|\033[31m:fire:\033[m|\033[32m:four_leaf_clover:\033[m|", use_aliases=True))
        for a in range(len(armaz[b])):
            print(f"{(a + 1) :>2}|{armaz[b][a]['nivel']:>2}|{armaz[b][a]['nome']:>17}|{armaz[b][a]['pvt'] :>2}|{armaz[b][a]['pa']:>2}|{armaz[b][a]['s']}|{(armaz[b][a]['pv'] + armaz[b][a]['s'] + armaz[b][a]['pa'])}")
        log.debug('mostrei a tabela')
        while True:
            log.debug(f'perguntando para {jog[b][0]}')
            imp = input(f'{jog[b][0]} escolha teus personagens\n(Separe por vírgula, 0 - tudo)\n')
            esc = imp.strip().split(',')
            n = False
            if imp == '':
                pass
            for c in range(0, len(esc)):
                #print(f"For {c} in range, and len(armaz[0]) == {len(armaz[0])}")
                if esc[c].isnumeric() == True:
                    esc[c]: int = int(esc[c])
                    if esc[c] <= len(armaz[b]):
                        if c == len(esc) - 1:
                            n = True
                            log.info('suave na nave, n')
                            #print(n)
                        pass
                    else:
                        log.info('lascou, not n')
                        break
                else:
                    log.info('lascou, not n')
                    break
            if n == True and len(esc) == config[1]:
                log.info('selecionano e mandano')
                if len(esc) == 1 and esc[0] == 0:
                    log.info('fui no len(esc) == 1 and esc[0] == 0:')
                    for a in range(0, len(armaz[b])):
                        jog[b].append(armaz[b][a].copy())
                elif len(esc) != 1 and esc[0] == 0:
                    log.info('fui no len(esc) != 1 and esc[0] == 0:')
                    for a in range(0, len(armaz[b])):
                        jog[b].append(armaz[b][a].copy())
                    for c in range(1, len(esc)):
                        jog[b].append(armaz[b][(esc[c] - 1)].copy())
                else:
                    log.info('fui no else:')
                    # print('considerei diferente de zero')
                    for c in esc:
                        jog[b].append(armaz[b][c - 1].copy())
                break
            if n == False:
                pass
init()
