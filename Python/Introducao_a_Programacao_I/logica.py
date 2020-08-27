def nao(a):
    """Retorna a negação de valores booleanos, puros ou em lista.
    :param a: recebe o valor para negá-lo
    """
    if type(a) == list:
        lista = []
        for c in range(len(a)):
            if a[c] == True:
                lista.append(False)
            else:
                lista.append(True)
        return lista
    elif type(a) == bool:
        if a == True:
            return False
        else:
            return True
    else:
        raise ValueError('Somente lista ou bool')


def disj(*args):
    """Retorna a disjunção de valores booleanos, puros ou em lista.
    :param args: recebe 2 valores para realizar a operação
    """
    args=list(args)
    if len(args) == 2:
        if type(args[0]) == list and type(args[1]) == list:
            if len(args[0]) != len(args[1]):
                raise Exception('LenDiferente')
            lista = []
            for c in range(len(args[0])):
                if args[0][c] == True:
                    lista.append(True)
                elif args[1][c] == True:
                    lista.append(True)
                else:
                    lista.append(False)
            return lista
        elif type(args[0]) == bool and type(args[1]) == bool:
            if args[0] == True:
                return True
            elif args[1] == True:
                return True
            else:
                return False
        else:
            raise ValueError
    else:
        raise TypeError(f'disj precisa de 2 argumentos, mas {len(args)} dados')


def conj(a, b):
    """Retorna a conjunção de valores booleanos, puros ou em lista.
    :param a: recebe o 1° valor
    :param b: recebe o 2° valor
    """
    if type(a) == list and type(b) == list:
        if len(a) != len(b):
            raise Exception('LenDiferente')
        lista = []
        for c in range(len(a)):
            if a[c] == True and b[c] == True:
                lista.append(True)
            else:
                lista.append(False)
        return lista
    elif type(a) == bool and type(b) == bool:
        if a == True and b == True:
            return True
        else:
            return False
    else:
        raise ValueError


def cond(a, b):
    """Retorna a condicional de valores booleanos, puros ou em lista.
    :param a: recebe o 1° valor
    :param b: recebe o 2° valor
    """
    if type(a) == list and type(b) == list:
        if len(a) != len(b):
            raise Exception('LenDiferente')
        lista = []
        for c in range(len(a)):
            if a[c] == True and b[c] == False:
                lista.append(False)
            else:
                lista.append(True)
        return lista
    elif type(a) == bool and type(b) == bool:
        if a == True and b == False:
            return False
        else:
            return True
    else:
        raise ValueError


def bicond(a, b):
    """Retorna a bicondicional de valores booleanos, puros ou em lista.
    :param a: recebe o 1° valor
    :param b: recebe o 2° valor
    """
    if type(a) == list and type(b) == list:
        if len(a) != len(b):
            raise Exception('LenDiferente')
        lista = []
        for c in range(len(a)):
            if a[c] == b[c]:
                lista.append(True)
            else:
                lista.append(False)
        return lista
    elif type(a) == bool and type(b) == bool:
        if a == b:
            return True
        else:
            return False
    else:
        raise ValueError


def taut(*args):
    """Retorna a tautologia de valores booleanos, puros ou em lista.
    :param args: recebe os valores, booleanos ou uma lista
    :return: para True, tautológico; para False, não tautológico
    """
    if len(args) == 1:
        if type(args[0]) == list or type(args[0]) == tuple:
            for c in args[0]:
                if c != True:
                    return False
                else:
                    pass
            return True
        else:
            raise TypeError('Para um argumento, só se aceitam Listas ou Tuplas.')
    else:
        for c in args:
            if type(c) == bool:
                pass
            else:
                raise TypeError('Para mais de um argumento, só se aceitam valores Booleanos')
        for c in args:
            if c != True:
                return False
            else:
                pass
        return True


def cont(*args):
    """Retorna a contradição de valores booleanos, puros ou em lista.
    :param args: recebe os valores, booleanos ou uma lista
    :return: para True, contraditório; para False, não contraditório
    """
    if len(args) == 1:
        if type(args[0]) == list or type(args[0]) == tuple:
            for c in args[0]:
                if c != False:
                    return False
                else:
                    pass
            return True
        else:
            raise TypeError('Para um argumento, só se aceitam Listas ou Tuplas.')
    else:
        for c in args:
            if type(c) == bool:
                pass
            else:
                raise TypeError('Para mais de um argumento, só se aceitam valores Booleanos')
        for c in args:
            if c != False:
                return False
            else:
                pass
        return True

def cot(a:list):
    """Retorna a contingência de valores booleanos, puros ou em lista.
    :param a: recebe os valores, booleanos ou uma lista
    :return: para True, contingente; para False, não contingente
    """
    if not taut(a) and not cont(a):
        return 'contingente'
    elif taut(a) and not cont(a):
        return 'tautológico'
    elif not taut(a) and cont(a):
        return 'contraditório'


def eq(a: list, b: list):
    if a == b:
        return True
    else:
        return False


# def argm(*args):
#     if len(args) >= 3:
#         for c in args:
#             if len(c) != len(args[-1]):
#                 raise TypeError('Ao menos uma das listas tem len() Diferente.')
#             else:
#                 pass
#         for c in range(len(args[-1])):
#             if args[-1][c]:
#                 for b in args[:-1]:
#                     if args[-1][c] a



def imp(a,b):
    if type(a) and type(b) == list:
        if len(a) == len(b):
            for c in a:
                if type(c) == bool:
                    pass
                else:
                    raise ValueError('Existe nas listas um valor não booleano')
            for c in b:
                if type(c) == bool:
                    pass
                else:
                    raise ValueError('Existe nas listas um valor não booleano')
            for c in range(len(a)):
                    if a[c] and not b[c]:
                            return False
            return True
        else:
            raise Exception('Len Diferente')
    elif type(a) and type(b) == bool:
        if a and not b:
            return False
        return True
    else:
        raise ValueError('A e B DEVEM ser ambos listas')

def rev(a: list):
    """Revelar o resultado em V para True e F para False."""
    for c in range(len(a)):
        if a[c] == True:
            print('V')
        else:
            print('F')


# em dev
# def gerar(i:int):
#     a = ['p','q','r','s','t','u','v','w','x','y','z']
#     for b in range(i-1, -1, -1):
#         lista=[]
#         if b == i-1:
#             for c in range(2**i):
#                 if c%2 == 0:
#                     lista.append(True)
#                 elif c%2 == 1:
#                     lista.append(True)
#         else:
#             a[i]
#         exec('a[b] = lista.copy()')
