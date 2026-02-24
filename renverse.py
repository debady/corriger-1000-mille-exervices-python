import random as rd 
tablo = []


nbreEntier  = rd.randint(10,20)
print('Saisir ',nbreEntier)

for i in range (nbreEntier):
    entier  = rd.randint(-100,500)
    print('entier ',i+1,' est ',entier)
    tablo.append(entier)

print("le tablo est ",tablo)
i = 0
j = nbreEntier-1

while  i<j:

    resp = tablo [i]
    tablo [i] =tablo[j]
    tablo[j] = resp


    i=i+1
    j=j-1
print("tablo renverse est ",tablo)