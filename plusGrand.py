nbreEntier  = 20
# *int (input('veuillez saisir le nbre d\'entier a entré ----->:'))

somme = 0
x = 0 
PG = 0
tab = []

while x< nbreEntier:
    print('veuillez saisir le ',x+1," ème entier :")
    entier = int(input('---->:'))
    somme=somme +entier
    tab.append(entier)

    if x==0:
        PG = entier
    else:
        if PG>entier:
            PG = PG 
        else:
            PG = entier
    x = x+1
print('la somme des ',nbreEntier,' entiers qui sont :',tab,' est ',somme)
print('et le plus grand est ',PG)
