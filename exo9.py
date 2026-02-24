import random as rd 
tab=[]

for i in range(101):
    nbre = rd.randint(-20,21)
    tab.append(nbre)

print(len(tab)," ",tab)

tpositif=[]
tnegatif=[]

for x in range(len(tab)):
    if tab[x]>0:
        tinter=str(tab[x])
        tpositif.append(tinter)
    elif tab[x]<=0:
        tinter=str(tab[x])
        tnegatif.append(tinter)
print()
print(" ".join(tpositif))
print(len(tpositif))
print()
print(" ".join(tnegatif))
print(len(tnegatif))