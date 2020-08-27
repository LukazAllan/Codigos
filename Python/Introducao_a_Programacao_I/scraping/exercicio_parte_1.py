# Author: Allan Lucas
# Python 3.6+
valor = {
    'gasolina':float(input('Para valores com virgula, use ponto.\nQuanto e o preço da gasolina: '))
    'etanol':float(input('Para valores com virgula, use ponto.\nQuanto e o preço do etanol: '))
}
valor_ = valor['etanol'] / valor['gasolina']
if valor_ > 0.7:
    print(f"Na sua cidade, é mais barato comprar Gasolina a R${valor['gasolina']}, que Etanol a R${valor['etanol']}")
elif valor_ < 0.7:
    print(f"Na sua cidade, é mais barato comprar Etanol a R${valor['etanol']}, que Gasolina a R${valor['gasolina']}")
else:
    print(f"Na sua cidade, não faz diferença comprar Gasolina e Etanol ambos a R${valor['gasolina']}")
