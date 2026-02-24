import random as rd
tableau = []
nbreEmployer=rd.randint(0,100)

salaireHaut = 0
nbreEmployerSalaireHaut=0
salaireMini=0


while True:
    print('veuillez saisir les heures de travail ')
    nbredetraivail =rd.randint(0,1000)
    # int(input('...:'))

    while nbredetraivail<0:
        print('heure de travail doit être supérieur ou égal à 0')
        nbredetraivail =rd.randint(0,1000)
        # int(input('...:'))

    print('veuillez saisir le taux horaire ')
    tauxHoraire =rd.randint(1,1000)
    # int(input('...:'))

    while tauxHoraire<0:
        print('le taux horaire doit être supérieur ou égal à 0')
        tauxHoraire =rd.randint(0,1000)
        # int(input('...:'))

    print('veuillez saisir la dette ')
    dette =rd.randint(0,1000000)
    # int(input('...:'))

    salaireBrut =(nbredetraivail*tauxHoraire)
    impot = salaireBrut*0.075
    salairenet = salaireBrut-(impot+dette) 

    tableau.append(salairenet)
    nbreEmployer = nbreEmployer+1

    salaireHaut = tableau[0]
    for i in range(1,len(tableau)):
        if tableau[i]>salaireHaut:
            salaireHaut=tableau[i]

    for x in range(len(tableau)):
        if tableau[x]==salaireHaut:
            nbreEmployerSalaireHaut = nbreEmployerSalaireHaut+1

    pourcentage = (nbreEmployerSalaireHaut*100)/nbreEmployer

    salaireMini = tableau[0]
    for y  in range(len(tableau)):
        if tableau[y] >salaireMini:
            salaireMini=tableau[y]


    print('voulez vous entré une autre données ? (O/N)')
    choix =input('...:')

    while choix !='O' and choix!='N':

        print('Veuillez taper O  pour continuer ou N pour arêter ')
        choix=input('..:')

    if choix =='N':
        print(len(tableau))
        print(tableau)
        print("le nombre d'employer est ",nbreEmployer)
        print("le salaire le plus élévé  est ",salaireHaut)
        print("le nombre d'employer ayant ce salaire est ",nbreEmployerSalaireHaut)
        print("son pourcentage est  ",pourcentage)
        print("le salaire le plus bas est   ",salaireMini)
        break  
