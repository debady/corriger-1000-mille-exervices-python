import random as rd 
tablo = []

nbreEntier  = rd.randint(1,200)
for i in range(nbreEntier):

    entier = rd.randint(0,500)
    tablo.append(entier)

print(tablo)

for j in range(0,nbreEntier):
    for i in range(j,nbreEntier):
        if tablo[i]<tablo[j]:
            resp = tablo[i]
            tablo[i]=tablo[j]
            tablo[j] = resp
print(tablo)
print()


