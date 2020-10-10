har: float = 0.0
num = 0
for c in range(201):
  har: float = 0.0
  for i in range(c):
    har += 1/(i+1)
  num=har*100+num
print(f"Lvl.{c} {har*100+num:.0f}")