chico:float    = 1.5
ze:float       = 1.1
cr_chico:float = 0.02
cr_ze:float    = 0.03
c:int          = 0

while chico > ze:
    chico = chico + cr_chico
    ze = ze + cr_ze
    c += 1
print(f"Serão Precisos {c} anos para Zé > Chico.")
    #if chico < ze:
        #print("STOP!!!!!!!!!!!!!!")
