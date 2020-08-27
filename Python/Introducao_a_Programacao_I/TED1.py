def leianum(txt:str = None, real:bool = True):
    if txt == None:
        if not real:
            txt = 'Digite um número Inteiro: '
        else:
            txt = 'Digite um número Real: '
    while True:
        try:
            if real:
                n = float(input(txt))
            else:
                n = int(input(txt))
            return n
        except ValueError:
            print('SOMENTE DIGITE NÚMEROS INTEIROS!')
        except KeyboardInterrupt:
            print('')
        except EOFError:
            pass


def tit(msg:str, hif:int = 35):
    print(f'{msg} ', end='')
    print('-' * (hif - len(msg)))


try:
    tit('TED 01')
    #---------2.--------------
    tit('Positivo ou Negativo')
    n = leianum(real = False)
    if n > 0:
        print(f'N = {n} é positivo!')
    elif n < 0:
        print(f'N = {n} é negativo!')
    else:
        print(f'N = 0 é neutro!')
    print('\n\n')
    #---------3.--------------
    tit('1° > (2° + 3°)')
    nums = []
    for c in range(3):
        nums.append(leianum(f'Digite 1 número real ({c}/3): '))
    if nums[0] > (nums[1] + nums[2]):
        print(f'{nums[0]} > ({nums[1]} + {nums[2]})')
    if nums[0] < (nums[1] + nums[2]):
        print(f'{nums[0]} < ({nums[1]} + {nums[2]})')
    else:
        print(f'{nums[0]} == ({nums[1]} + {nums[2]})')
    print('\n\n')
    #---------4.--------------
    tit('Faixa Etária')
    id = -1
    while id <= 0:
        id = leianum('Você quer ser um nadador profissional?\nnos infome sua idade para inscrevê-lo: ', False)
    if id < 5:
        print('Não é possivel inscrever-te! Você não tem idade mínima!')
    elif 5 <= id < 8:
        print('Parabéns, agora tu estás inscrito.\nTua categoria é: INFANTIL A,\nboa sorte!')
    elif 8 <= id < 11:
        print('Parabéns, agora tu estás inscrito.\nTua categoria é: INFANTIL B,\nboa sorte!')
    elif 11 <= id < 14:
        print('Parabéns, agora tu estás inscrito.\nTua categoria é: JUVENIL A,\nboa sorte!')
    elif 14 <= id <= 17:
        print('Parabéns, agora tu estás inscrito.\nTua categoria é: JUVENIL B,\nboa sorte!')
    elif id > 17:
        print('Parabéns, agora tu estás inscrito.\nTua categoria é: SÊNIOR,\nboa sorte!')
    print('\n\n')
    #---------5.--------------
    nums = []
    for c in range(5):
        n = leianum()
        if n > 10:
            nums.append(n)
    if len(nums) != 0:
        print(f'números > 10 in nums: {nums}')
    print('\n\n')
    #---------6.--------------
    tit('Diferença do maior pelo menor')
    n1 = float(input('Número para n1: '))
    n2 = float(input('Número para n2: '))
    if n1 > n2:
        print(f'Δn = {n1-n2}')
    elif n1 < n2:
        print(f'Δn = {n2-n1}')
    else:
        print('Δn = 0')
    print('\n\n')
    #---------7.--------------
    
    print('\n\n')
    #---------8.--------------
    print('\n\n')
    #---------9.--------------
    print('\n\n')
except KeyboardInterrupt:
    print('O Usuário interrompeu  processo com Ctrl + C!\nVolte Sempre!')
except EOFError:
    print('O Usuário interrompeu  processo com Ctrl + Z!\nVolte Sempre!')
