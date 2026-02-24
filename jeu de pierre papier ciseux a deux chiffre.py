import random
hazards1=random.randint(1, 3)
hazards2=random.randint(1, 3)
victoire_joueur1=0
aucun_gain=0
victoire_joueur2=0
nul=0
nom1=input("joueur 1 veuillez saisir votre noms : ")
nom2=input("joueur 2 veuillez saisir votre noms : ")
while True:
    print(nom1, ": ",victoire_joueur1," points // egalié : ",nul," points //",nom2 , " : " ,victoire_joueur2," points // aucun_gain: ",aucun_gain )
    print("veuillez choisir un un chiffre entre ")
    print("1") 
    print("2") 
    print("3") 
    print("ou")
    print("quitter")
    print("REGLES 1 ) si votre chiffre coresponds a celui choisir par l'ordinateur vous avez gagné +1 points")
    print("REGLES 2 )par consequant si ce n'est aps le cas vous avez perdu +0 points")
    print("REGLES 3 )si vous avez fait tout les deux de bon choir alors vous ettes a egalité .eagalité +1")
    print("REGLES 4 )si vous avez fait un mauvais choix -1")
    print("REGLES 3 )si vous abadonner la partir -1")
    
    if hazards1==1:
        choix_ordi1="pierre"
    elif hazards1==2:
        choix_ordi1="papier"
    elif hazards1==3:
        choix_ordi1="ciseaux"
        
        
    if hazards2==1:
        choix_ordi2="pierre"
    elif hazards2==2:
        choix_ordi2="papier"
    elif hazards2==3:
        choix_ordi2="ciseaux"
        
        
        
    print(nom1,"veuillez saisir un chiffre : ")
    coup_joueur1=int(input())
    if coup_joueur1=="quitter":
        print(nom1,"a quitter la partie")
        victoire_joueur1=victoire_joueur1-1
        break
    elif coup_joueur1!=1 and coup_joueur1!=2and coup_joueur1!=3:
        print("desolé ",nom1," veuillez saisir un coup correct ! ")
        victoire_joueur1=victoire_joueur1-1
        continue
        
        # condition d'affiche du joueur 2
        
    print(nom2,"veuillez saisir un chiffre : ")
    coup_joueur2=int(input())
    if coup_joueur2=="quitter":
        print(nom2,"a quitter la partie")
        victoire_joueur2=victoire_joueur2-1
        break
    elif coup_joueur2!=1 and coup_joueur2!=2 and coup_joueur2!=3:
        print("desolé ",nom2," veuillez saisir un coup correct ! ")
        victoire_joueur2=victoire_joueur2-1
        continue
    
    
        #condition de gains 
        
        
    if coup_joueur1==choix_ordi1 and coup_joueur2==choix_ordi2:
        print(choix_ordi1 ,"--VS--",choix_ordi2)
        print("egalié ")
        nul=nul+1
    elif coup_joueur1==choix_ordi1 and coup_joueur2!=choix_ordi2:
        print(choix_ordi1 ,"--VS--",choix_ordi2)
        print("bravo ! ",nom1,"vous avez gagné ")
        victoire_joueur1=victoire_joueur1+1
    elif coup_joueur1!=choix_ordi1 and coup_joueur2==choix_ordi2:
        print(choix_ordi1 ,"--VS--",choix_ordi2)
        print("bravo ! ",nom2,"vous avez gagné ")
        victoire_joueur2=victoire_joueur2+1
    elif coup_joueur1!=choix_ordi1 and coup_joueur2!=choix_ordi2:
        
        print(nom1,"vous aurai du choisir",hazards1 ,"--VS--",nom2,"vous aurai du choisir",hazards2)
        print("vous avez tout deux perdu ! ")
        aucun_gain=aucun_gain+1
        