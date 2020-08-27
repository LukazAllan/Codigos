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
