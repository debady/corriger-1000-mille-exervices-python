import random as rd
lettre = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=''
tab=[]

for i in range(0,10):
    taille = len(a)

    if taille<5:
        nbre = rd.randint(0,25)
        a=a+lettre[nbre]    

    if taille>=5:
        tab.append(a)
        taille=0
        a=''
        print(tab)

# tabNom =[]

# x= 0
# a=''
# taille =0

# while  x<100:

#     genere=rd.randint(0,25)
#     a=a+lettre[genere]

#     taille=len(a)

#     if taille%5==0:
#         tabNom.append(a)
#         a=''
#         taille=0
#     x=x+1

# nbreNote = 3*(100/5)
# tabNote= []

# while nbreNote>0:
#     note =rd.randint(0,21)
#     tabNote.append(note)
#     nbreNote=nbreNote-1
# print(tabNote)

# c =0
# tablFusion ={}
# while c<len(tabNom):
#     tablFusion[tabNom[c]] =tabNote[2]
#     tablFusion.append(tabNom[c])
#     # tablFusion.append(' NOTE :')
#     # tablFusion.append(tabNote[c])


# print(tablFusion)
# # print(len(tabNom))

# import random as rd 
# tabNom = []
# tabMoy = []

# nbreEtud =rd.randint(-5,20)
# #  int(input('Veuillez saisir le nombre d\'étudiant :'))
# print(nbreEtud)
# while nbreEtud <0:
#     print('veuillez saisir un nombre positif')
#     nbreEtud =rd.randint(-5,20)
#     print(nbreEtud)

#     #  int(input('Veuillez saisirà une valeur positif :'))
# nomEtud= ''
# taile = 0
# for i in range(nbreEtud):
#     generer = rd.randint(0,25)
#     print('veuillez saisir le nom ',i+1)
#     nomEtud = nomEtud+lettre[generer]

#     taille  = len(nomEtud)
#     if taille %5==0:
#         print(nomEtud)
#         print(taille)
#         tabNom.append(nomEtud)
#         nomEtud=''
#         taille = 0
        

#     somme = 0
#     for j in range(3):
        
#         print('veuillez saisir la note ',j+1)
#         note = rd.randint(0,20)
#         print(note)
#         #  int(input('...:'))
#         somme = somme + note
#     tabMoy.append(somme/3)

#     print(nomEtud,'somme',somme,'moyenne',somme/3)
#     print()

# print(tabNom)
# moyp = tabMoy[1]
# nomp = tabNom[1]
# cpt = 0

# # if tabMoy[1]>=10:
# #     cpt=cpt+1


# for i in range(0,nbreEtud-1):
#     if tabMoy[i]>moyp:
#         moyp=tabMoy[i]
#         # nomp=tabNom[i]

#     if tabMoy[i]>=10:
#         cpt=cpt+1
# pcent = (cpt*100)/nbreEtud

# print('1: pour la moyenne du premier')
# print('2: pour le nombre de personne ayant la moyenne et le pourcentage')

# print('faites votre choix')
# choix = input('...:')

# while choix !='1' and choix !='2':
#     choix = input('veuillez choisir 1 ou 2')

# if choix =='1':
#     print('le nom du premier est ',nomp,'sa moyenne est ',moyp)
# elif choix == '2':
#     print('le nombre de personne ayant la moyenne est ',cpt,' le pourcentage est ',pcent)

# print('')
# print('')
# print("nombre etudiant",nbreEtud)
# print("les moyennes ",tabMoy)
# print("les noms ",tabNom)
# print("nombre de personne ayant la moyenne ",cpt)
# print("pourcentage ",pcent)