import random as rd 
print('Combien d\'entier vouslez-vous saisir :')

nbreEntier= rd.randint(-10,20)
print(nbreEntier)

while nbreEntier<1:
    nbreEntier=rd.randint(-10,20)

x=0
tab=[]

while x<nbreEntier:
    print('veuillez saisir le,',x+1,' ème entier')
    entier =rd.randint(-99999,100000)
    print(entier)
    tab.append(entier)
    x=x+1

valMin = tab[0]

for i in range(0,nbreEntier):
    if tab[i]<valMin:
        valMin=tab[i]
        posi=i
    else:
        valMin=valMin
# s=0
# while s<nbreEntier:
#     if tab[s]<valMin:
#         valMin=tab[s]
#         posi=s
#     s=s+1
print(tab)
print('le nombre le plus petit est',valMin,' et il a été saisir pour la dernière fois à la position',posi+1)