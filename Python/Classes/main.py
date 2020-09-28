# Author: Allan Lucas
# Python 3.8.2

class Caneta:
    def __init__(self):
        self.modelo = "bic"
        self.cor = "vermelho"
        self.carga = 100
        self.tampada = True
        pass
    
    def rabiscar(self):
        if self.tampada:
            Exception("Não se escreve com a caneta tampada!")
        elif self.carga <= 0:
            Exception("Não se escreve sem tinta!")
        print("^v^v^v^v^v^v^v^vrabiscando aq!")
    
    def tampar(self):
        self.tampada = True
    
    def destampar(self):
        self.tampada = False