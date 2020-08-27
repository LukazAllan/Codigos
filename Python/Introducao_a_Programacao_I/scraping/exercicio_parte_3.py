# Author: Allan Lucas
# Python 3.6+

print('Para valores com virgula, use ponto.')
valor = valor = {
    'gasolina':float(input('Quanto é o preço da gasolina: ')),
    'etanol': float(input('Quanto e o preço do etanol: '))
}
cap_max = float(input('Quanto e a capacidade maxima do seu veiculo, em litros: '))
km_l = {
    'gasolina':float(input('Com quantos quilometros de Gasolina seu veiculo anda por litro? ')),
    'etanol':float(input('Com quantos quilometros de Etanol seu veiculo anda por litro? '))
}
auto = {
    'gasolina':cap_max*km_l['gasolina'],
    'etanol':cap_max*km_l['etanol']
}
distancia = 764
print(f"""
Numa viagem entre João Pessoa e Salvador, de {distancia}km

Usando Gasolina em toda a viagem, se começar a viagem com o tanque cheio:
você vai parar {int((distancia-auto['gasolina'])/auto['gasolina'])} vezes para abastecer.
Gastará em média: R${int((distancia-auto['gasolina'])/auto['gasolina'])*valor['gasolina']*cap_max:.2f}

Usando Etanol em toda a viagem, se começar a viagem com o tanque cheio:
você vai parar {int((distancia-auto['etanol'])/auto['etanol'])} vezes para abastecer.
Gastará em média: R${int((distancia-auto['etanol'])/auto['etanol'])*valor['etanol']*cap_max:.2f}
""")
