#ver 1.1.5
from canivete import rinput

data_cont = list()
query = rinput('Jogo: Amistoso / Campeonato ', ['a', 'c'], '>>')

if query == 'a':
    import amistoso
    amistoso.init()
else:
    import campeonato
    campeonato.init(data_cont)
