class Personagem:
    "Dá características de personagem à estrurura de dados."

    def __init__(self, nome):
        self.nome = nome
        pass

    def relacao(self, pessoa: Personagem):
        self
