# altura sexo
# menor altura
# maior altura
# média altura mulheres
# média altura pop.
# percentual de hom
c:int = 0
f:int = 0
m:int = 0
sex:int = -1
pop:int = 5
menor_altura:float = 0.0
maior_altura:float = 0.0
med_pop:float = 0.0
med_f:float = 0.0
pc_h:float = None
alt:float = 0.0

while c < pop:
  alt = float(    input("digite sua altura: ")     )
  sex = int(input("0 - Masculino\n1 Feminino\n>> "))
  
  if c == 0:
    menor_altura = alt
    maior_altura = alt
  else:
    if alt < menor_altura:
      menor_altura = alt
    
    if alt > maior_altura:
      maior_altura = alt
  
  med_pop = med_pop + alt
  
  if sex == 1:
    f = f+1
    med_f = med_f + alt
  else:
    m = m+1
  
  c+=1

med_pop = med_pop / pop
med_f = med_f / f
pc_h = m / pop * 100
print(f"""Resultados:\n
maior altura encontrada           : {maior_altura}\n
menor altura encontrada           : {menor_altura}\n
média de altura das mulheres      : {med_f}\n
média de altura da população      : {med_pop}\n
percentual de homens na população : {pc_h}%""")