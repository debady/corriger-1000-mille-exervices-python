while True:

    nbreReel = int(input('Veuillez saisir le nombre de notes MAX 100:'))
    while nbreReel>100:
        nbreReel = int(input('Pas plus que 100 ! réessayer :'))

    i=0
    som=0
    tab=[]

    for i in range(0,nbreReel+1):
        print("veuillez saisir la ",i+1," ème valeur")    
        val=float(input("...:"))
        tab.append(val)
        som=som+tab[i]
        # som=som+val

    valMini=tab[0]
    for i in range(0,nbreReel+1):
        if valMini>=tab[i]:
            valMini=tab[i]

    moy=som/nbreReel
    j=0
    for i in range(0,nbreReel+1):
        if tab[i]>=moy:
            j=j+1

    pourcent =(j*100)/nbreReel
    print('M : pour moyenne ')
    print('P : pour PLUS pétite ')
    print('N : pour nbre de note supérieur à la moyenne et le pourcentage')
    resp = input('..:')

    while resp !="M" and resp !="P" and  resp !="N" :
        print('Erruer ! \nM : pour moyenne ')
        print('P : pour PLUS pétite ')
        print('N : pour nbre de note supérieur à la moyenne et le pourcentage')
        resp = input('..:')

    if resp =="M" :
        print('la moyenne est :',moy)

    elif resp =="P" :
        print('la plus pétite valeur :',valMini)

    elif resp =="N" :
        print('le nombre de note supérieur à la moyenne est  :',j)


    print('\nles éléments du tableau sont :',tab)
    print('la somme est  :',som)
    print('la moyenne est :',moy)
    print('la plus pétite valeur :',valMini)
    print('le nombre de note supérieur à la moyenne est  :',j)

