import random
from random import randint
victoire_joueur1=0
victoire_joueur2=0
nul=0
hazards=random.randint(1, 3)
nom1=input("joueur 1 veuillez saisir votre noms : ")
nom2=input("joueur 2 veuillez saisir votre noms : ")
while True:
    print(nom1, ": ",victoire_joueur1," points // egalié : ",nul," points //",nom2 , " : " ,victoire_joueur2," points" )
    print("LISTS DES COUPS ")
    print("pierre")
    print("papier")
    print("ciseaux")
    print("ou")
    print("quitter")
    
    
    print(nom1,"veuillez saisir votre coup entre : ")
    coup_joueur1=input()
    if coup_joueur1=="quitter":
        print(nom1,"a quitter la partie")
        victoire_joueur1=victoire_joueur1-1
        break
    elif coup_joueur1!="pierre" and coup_joueur1!="papier" and coup_joueur1!="ciseaux":
        print("desolé ",nom1," veuillez saisir un coup correct ! ")
        victoire_joueur1=victoire_joueur1-1
        continue
    elif coup_joueur1=="pierre":
        print("PIERRE---vs--", end=" ")
    elif coup_joueur1=="papier":
        print("papier---vs--", end=" ")
    elif coup_joueur1=="ciseaux":
        print("ciseaux---vs--", end=" ")
        
        
        
        
    print(nom2,"veuillez saisir votre coup entre : ")
    coup_joueur2=input()
    if coup_joueur2=="quitter":
        print(nom2," a quitter la partir .")
        victoire_joueur2=victoire_joueur2-1
        break
    elif coup_joueur2!="pierre" and coup_joueur1!="papier" and coup_joueur1!="ciseaux":
        print("desolé ",nom2," veuillez saisir un coup correct ! ")
        victoire_joueur2=victoire_joueur2-1
        continue
    elif coup_joueur2=="pierre":
        print("PIERRE---vs--", end=" ")
    elif coup_joueur2=="papier":
        print("papier---vs--", end=" ")
    elif coup_joueur2=="ciseaux":
        print("ciseaux---vs--", end=" ")
        
        
    if coup_joueur1==coup_joueur2:
        print("egalité")
        nul=nul+1
        
        
    hazards=random.randint(1, 3)
    if hazards==1:
        coup_pc="pierre"
        print(" pierre")
    elif hazards==2:
        coup_pc="feuille"
        print(" feuille")
    elif hazards==3:
        coup_pc="ciseaux"
        print(" ciseaux")
    
    
    
print("veuillez saisir un chiffre entre ")  

joueur1=int(input())
