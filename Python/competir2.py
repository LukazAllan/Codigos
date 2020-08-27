from random import randint as rd
from time import sleep as dly

A0Z25 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
data =[]
p=[['Allan',0], ['Bruno',0], ['Carlos',0], ['Diego',0],
    ['Elton',0], ['Fabiano',0], ['Nicolas',0], ['Miguel',0],
    ['Vitor',0], ['Pedro',0], ['Gustavo',0], ['Guilherme',0],
    ['Eduardo',0], ['Thiago',0], ['Rodrigo',0], ['Igor',0],
    ['Júlio',0], ['Heitor',0], ['Luiz',0], ['Rafael',0],
    ['Davi',0],['Luan',0], ['Yuri',0],['Paulo',0],
   ['Henrique',0], ['Celso',0], ['Daniel',0], ['Caio',0],
   ['Lucas',0], ['Alec',0], ['Enzo',0], ['Jânio',0]]
a = p.copy()
#por exemplo, 31 part., dividir em grupos c 4 integrantes
integrantes =4
total=len(a)#32
grupos=len(a)//integrantes
for grupo in range(grupos):#4 = grupos
    g=[]
    for c in range(integrantes):#4 = integrantes nos grupos
        if not len(a) == 0:
            al = rd(0, len(a)-1)
        else:
            al=0
        g.append(a[al])
        a.remove(a[al])
    data.append(g)

if len(a) != 0:
    data.append(a)
    a = []
cont = 0
for c in data:
    dly(1)
    print(f'Grupo {A0Z25[cont]}:')
    for b in range(len(c)):
        dly(0.5)
        print(f'{b+1}.{c[b][0]}')
    cont += 1
    print('')

pto = lambda ponto: ponto[1]
for a in range(len(data)):
	camp=data[a].copy()
	print(f'Disputas Grupo {A0Z25[a]}')
	for c in range(len(camp)):
		op = camp[c+1:len(camp)].copy()
		for b in range(len(op)):
			res=[0,0]
			print(f'{camp[c][0]} vs. {op[b][0]}')
			while res[0] == res[1]:
				res = [rd(0,100),rd(0,100)]
			dly(3)
			if res[0] > res[1]:
				camp[c][1] += 1
				print(f'{camp[c][0]} vence!\n')
			else:
				camp[c+b+1][1] += 1
				print(f'{camp[c+b+1][0]} vence!\n')
	camp.sort(key=pto, reverse=True)
	data[a] = camp.copy()
	for c in range(len(camp)):
		print(f'{c+1}. {camp[c][0]}  {camp[c][1]}')
	print('')
	dly(1)
	pontos=[]
	for c in camp:
		pontos.append(c[1])
	if pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
		desempate = 1
		while pontos.count(1) == 3 or pontos.count(2) == 3 and len(pontos) != 3 or pontos.count(2) == 2 and pontos[0] == 3:
			if pontos.count(1) == 3 and len(pontos) != 3:
				camp=data[a][1:].copy()
			elif pontos.count(2) == 3 and len(pontos) != 3:
				camp=data[a][:3].copy()
			elif pontos.count(2) == 2 and pontos[0] == 3:
				camp=data[a][1:3].copy()
			print(f'Desempate {desempate} Grupo {A0Z25[a]}')
			for c in range(len(camp)):
				op = camp[c+1:len(camp)].copy()
				for b in range(len(op)):
					res=[0,0]
					print(f'{camp[c][0]} vs. {op[b][0]}')
					while res[0] == res[1]:
						res = [rd(0,100),rd(0,100)]
					dly(3)
					if res[0] > res[1]:
						camp[c][1] += 1
						print(f'{camp[c][0]} vence!\n')
					else:
						camp[c+b+1][1] += 1
						print(f'{camp[c+b+1][0]} vence!\n')
			camp.sort(key=pto, reverse=True)
			for c in range(len(camp)):
				print(f'{c+1}. {camp[c][0]}  {camp[c][1]}')
			print('')
			pontos=[]
			for c in camp:
				pontos.append(c[1])
			if pontos.count(1) != 3 or pontos.count(2) != 3 and len(pontos) == 3 or pontos.count(2) != 2 and pontos[0] != 3:
				if pontos.count(1) == 3:
					for x in range(len(camp)):
						data[a][x+1] = x.copy()
				elif pontos.count(2) == 3 and len(pontos) != 3:
					for x in range(len(camp)):
						data[a][x] = x.copy()
				elif pontos.count(2) == 2 and pontos[0] == 3:
					for x in range(len(camp)):
						data[a][x+1] = x.copy()
			else:
				pass
			dly(1)
	else:
		pass
	dly(1)
for c in range(len(data)):
	dly(1)
	print(f'Grupo {A0Z25[c]}')
	for b in range(len(data[c])):
		dly(1.5)
		print(f'{b+1}. {data[c][b][0]} {data[c][b][1]}')
	print('')
