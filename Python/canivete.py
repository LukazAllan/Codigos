from os import path, system


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
        os.system('clear')
    if windows:
        os.system('cls')


def limpa():
    """
    Função que limpa a tela
    """
    if path.isdir('C:/'):
        system('cls')
    if path.isdir('/storage/emulated/0/'):
        system('clear')


def linque(caminho, form='r', ascii=True):
    """
    Função que linca o arquivo
    :param caminho: indica o caminho do arquivo
    :param ascii: leitura de códigos ascii, que
    para ativar escreva False para ele
    :return: a
    """
    if path.isfile(caminho, form):
        return open(caminho, form, ensure_ascii=ascii)


def pc():
    if path.isdir('C:/'):
        return 'windows'
    elif path.isdir('/storage/emulated/0/'):
        return 'android/linux'


def rinput(texto, b=None):
    """
    Função que não para de executar input
    até que você digite alguma coisa ou
    digite a coisa correta.
    :type texto: object
    :param texto: Exibe no input
    :type b: object
    :param b: lista de condição
    :return: var c
    """
    if b is None:
        b = list()
    cont = -1
    while True:
        cont += 1
        if cont == 0:
            c = input(f'{texto}: ')
        else:
            c = input(f'Tente novamente.\n{texto}: ')
        if c == '':
            li()
            pass
        else:
            if not b:
                return str(c)
            else:
                if c in b:
                    return str(c)
                else:
                    pass

