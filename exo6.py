import random as rd
n = rd.randint(1,1000)

print("le nombre d'élément est",n)
tab=[]
l=1
while n>0:
    print('veuillez saisir le ',l,' ème entier')

    entier = rd.randint(0,10000)
    print(entier)

    tab.append(entier)
    n=n-1
    l=l+1
print('taper ')
print('R : pour rechercher une valeur dans le tableau')

print('I : pour inversé les élément du tableau')
print('T : pour trié les élément du tableau')

print('Q : pour quitter le programme')

rep =input('..:')
while rep != 'R' and rep != 'I' and  rep != 'T' and rep != 'Q':

    print('Vous devriez choisir entre R,T,I ou Q')
    rep=input()

if rep=='I':

    TabInverse = []
    p=len(tab)-1

    while p>=0:
        TabInverse.append(tab[p])

        p=p-1
    print('L\'inverse du tableau est ',TabInverse)
if rep=='Q':
    print('Vous avez quitter le programme')

if rep=='R':
    print('Veuillez saisir la valeur à rechercher ')

    v= int(input('...:'))
    x= 0

    for i in range (len(tab)):
        if tab[i]==v:
            x=x+1
    if x>0:
        print(v,' est dans le tableau ')
    else:
        print(v,'n\'est pas dans le tableau')
if rep=='T':
    tab=sorted(tab)
    print("le tableau trié esr ",tab)