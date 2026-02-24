import random as rd
tablLettre  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# tablNom = []
# nom = ''

# for i in range (6): # nombre de lettre d'un nom
#     while len(tablNom)<7:
#         for j in range(5):
#             posiLettre = rd.randint(0,25)
#             nom = nom +tablLettre[posiLettre]

#             taille = len(nom)
#             if taille ==5:
#                 tablNom.append(nom)
#                 nom = ''
#                 taille = 0
# print(tablNom)


tabloMoy = []
tabloNom = []
som = 0
cpt = 0
nomEtud = ''

nbreEtdud = rd.randint(5,10)
print('Le nombre d\'etudiants est ',nbreEtdud)
# * int(input('Veuillez saisir le nombre d\'etudiant  :'))
for  i in range(nbreEtdud):
    print()
    for  t in range (6): # nombre de lettre d'un nom 5
        while len(tabloNom)<nbreEtdud:
            print()
            print('Veuillez saisir la nom du ',i+1,' ème étudiant' )
            for x in range(nbreEtdud): # nbre etudiant
                
                posiLettre = rd.randint(0,25)
                nomEtud = nomEtud+tablLettre[posiLettre]

                taille = len(nomEtud)
                if taille == 5:
                    tabloNom.append(nomEtud)
                    print(nomEtud)
                    nomEtud =''
                    taille =0


    # nomEtud = input("....:")
    # tabloNom.append(nomEtud)

                    som = 0
                    moy = 0
                    for j in range(3):
                        print('veuillez saisir la ',j+1,' note de ',tabloNom[i])

                        note = rd.randint(0,20)
                        print(note)
                        
                        # float(input('...:'))
                        som =som +note

                    moy = som / 3
                    if moy >=10:
                        cpt = cpt+1
                    tabloMoy.append(moy)
    # print()

#  recherche du premier 
moyp = tabloMoy[0]
nomP = tabloNom[0]

for i in range(1,nbreEtdud):
    if moyp <tabloMoy[i]:
        moyp=tabloMoy[i]
        nomP = tabloNom[i]
print("le nombre d\'etudiant est ",nbreEtdud)
print("le nmbre de ceux qui ont la moyenne sont ",cpt)
print("le premier est ",nomP,"sa moyenne est ",moyp)
print()r
print('les noms sont ',tabloNom)
print('les moyennes sont ',tabloMoy,)