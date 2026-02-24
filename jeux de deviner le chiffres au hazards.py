import random
choix1=random.randint(100, 500)
choix2=random.randint(100, 500)
nbre_tentetives=10
nbre_tentetives1=10
nbre_tentetives2=10
m=nbre_tentetives
victoire_joueur1=0
victoire_joueur2=0
nul=0
print()
nom1=input("JOUEUR N°1 veuillez saisir votre nom :")
nom2=input("JOUEUR N°2 veuillez saisir votre nom :")
print()
print("vous avez 10 tentatives afin de trouvez le nombres correct")
print("le n-nieme tentatives est votre points que vous gagné ! ")
print()
i=0
while nbre_tentetives>0:
    print(nom1," : ",victoire_joueur1,"points ::: egalité : ",nul, " points ::: ",nom2," : ",victoire_joueur2," points")
    print()
    print(nom1," votre ",i+1,"eme esais: entrz votre nombres : ")
    quest1=input()
    quest1=int(quest1)
    print(nom2," votre ",i+1,"eme esais: entrz votre nombres : ")
    quest2=input()
    quest2=int(quest2)
    print()
    
    
    
    if quest1<choix1  and quest2<choix2:
        print(nom1,quest1,"est petit.c'est plus")
        print(nom2,quest2,"est petit.c'est plus")
        nul=nul+1
    elif quest1<choix1  and quest2>choix2:
        print(nom1,quest1,"est petit.c'est plus")
        print(nom2,quest2,"est grands.c'est moins")
        nul=nul+1
    elif quest1>choix1  and quest2<choix2:
        print(nom1,quest1,"est grands.c'est moins")
        print(nom2,quest2,"est petit.c'est plus")
        nul=nul+1
        
        
    elif quest1>choix1 and quest2>choix2:
        print(nom1,quest1,"est grands.c'est moins")
        print(nom2,quest2,"est grands.c'est moins")
        nul=nul+1
        print()
    else:
        break
    nbre_tentetives=nbre_tentetives-1
    i=i+1
if nbre_tentetives1 !=0 and quest1==choix1:
    print("bravo",nom1," vous avez trouvez ",choix1," au",10-nbre_tentetives1," eme essaies")
    victoire_joueur1=victoire_joueur1+1
    print(nom1," : ",victoire_joueur1,"points ::: egalité : ",nul, " points ::: ",nom2," : ",victoire_joueur2," points")

else:
    print(nom1,"houp! vous n'avez pas trouvez les 10 tentatives sont epuisé .c'etais",choix1)
    print(nom1," : ",victoire_joueur1,"points ::: egalité : ",nul, " points ::: ",nom2," : ",victoire_joueur2," points")

    
if nbre_tentetives2 !=0 and quest2==choix2:
    print("bravo",nom2," vous avez trouvez ",choix2," au",10-nbre_tentetives2," eme essaies")
    victoire_joueur2=victoire_joueur2+1
    print(nom1," : ",victoire_joueur1,"points ::: egalité : ",nul, " points ::: ",nom2," : ",victoire_joueur2," points")

else:
    print(nom2,"houp! vous n'avez pas trouvez les 10 tentatives sont epuisé .c'etais",choix2)
    nul=nul+1
    print(nom1," : ",victoire_joueur1,"points ::: egalité : ",nul, " points ::: ",nom2," : ",victoire_joueur2," points")

    while True:
        q=input("voulez vous continuer : ")
        if q=="oui":
            continue
        else:
            break 
        print(nom1," : ",victoire_joueur1,"points ::: egalité : ",nul, " points ::: ",nom2," : ",victoire_joueur2," points")