# Author: Allan Lucas
# Python 3.6+

cap_max = float(input('Para valores com virgula, use ponto.\nQuanto e a capacidade maxima do seu veiculo, em litros: '))
km_l = {
    'gasolina':float(input('Com quantos quilometros de Gasolina seu veiculo anda por litro? ')),
    'etanol':float(input('Com quantos quilometros de Etanol seu veiculo anda por litro? '))
}
auto = {
    'gasolina':cap_max*km_l['gasolina'],
    'etanol':cap_max*km_l['etanol']
}
print(f"Em media, seu carro anda com tanque cheio em gasolina: {auto['gasolina']}km, e em etanol: {auto['etanol']}km")
