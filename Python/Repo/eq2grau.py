from json import dump
file = open('eq2grau.json', 'w')
data = list()
contador = 0
minimum: int = 1
maximum: int = 100
for a in range(minimum, maximum+1):
    if a != 0:
        for b in range(minimum, maximum+1):
            for c in range(minimum, maximum+1):
                delta = (b**2)-(4*a*c)
                if delta > 0:
                    if (-b + delta**(1/2))/(2*a) == int((-b + delta**(1/2))/(2*a)) and\
                            (-b - delta**(1/2))/(2*a) == int((-b - delta**(1/2))/(2*a)) and\
                            (-1*b)/(2*a) == int((-1*b)/(2*a)) and (delta*-1)/(4*a) == int((delta*-1)/(4*a)):
                        if a != 1:
                            if b == 0:
                                if c != 0:
                                    data.append(f'{a}x² + {c} = 0')
                                else:
                                    data.append(f'{a}x² = 0')
                            elif b == 1:
                                if c != 0:
                                    data.append(f'{a}x² + x + {c} = 0')
                                else:
                                    data.append(f'{a}x² + x  = 0')
                            else:
                                if c != 0:
                                    data.append(f'{a}x² + {b}x + {c} = 0')
                                else:
                                    data.append(f'{a}x² + {b}x  = 0')

                        else:
                            if b == 0:
                                if c != 0:
                                    data.append(f'x² + {c} = 0')
                                else:
                                    data.append(f'x² = 0')
                            elif b == 1:
                                if c != 0:
                                    data.append(f'x² + x + {c} = 0')
                                else:
                                    data.append(f'x² + x  = 0')
                            else:
                                if c != 0:
                                    data.append(f'x² + {b}x + {c} = 0')
                                else:
                                    data.append(f'x² + {b}x  = 0')
                        contador += 1
                    else:
                        pass
                    """
                        if (-b + delta**(1/2))/(2*a) == (-b - delta**(1/2))/(2*a):
                            print(f'x = {(-b + delta**(1/2))/(2*a)}', end=', ')
                        else:
                            print(f'x1 = {(-b + delta**(1/2))/(2*a)} e x2 = {(-b - delta**(1/2))/(2*a)}', end=', ')
                        print(f'vértice em ({(-1*b)/(2*a)}, {(delta*-1)/(4*a)})')"""
                else:
                    pass
    else:
        pass
if contador == 0:
    print('Nenhuma equação do 2° grau encontrada!')
elif contador == 1:
    print(f'{contador} equação do 2° grau encontrada!')
else:
    print(f'{contador} equações do 2° grau encontrados!')
dump(data, file, ensure_ascii=False)
file.close()
