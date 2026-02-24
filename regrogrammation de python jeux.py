import random
user_victoire1=0
user_victoire2=0
pc_victoire=0
nul=0
nom1=input("JOUEUR 1 : VEUILLEZ SAISIR VOTRE NOM : ")
nom2=input("JOUEUR 2 : VEUILLEZ SAISIR VOTRE NOM : ")
while True:
    print()
    print(nom1 ," : " ,user_victoire1," points /  nul : " ,pc_victoire," points / " ,nom2 ," : " ,user_victoire2," points / " )
    print()
    print(nom1,"veuillez saisir votre coup entre : ")
    print()
    print("PIERRE")
    print("FEUILLE")
    print("CISEAUX")
    print("ou")
    print("quitter")
    print()
    coup_joueur1=input("------> ")
    print()
    print(nom2,"veuillez saisir votre coup entre : ")
    print()
    print("PIERRE")
    print("FEUILLE")
    print("CISEAUX")
    print("ou")
    print("quitter")
    print()
    coup_joueur2=input("------> ")
    if coup_joueur1=="quitter":
        print(nom1, "vous avez quitter le jeu ")
        break
    elif coup_joueur2=="quitter":
        print(nom2, "vous avez quitter le jeu ")
    elif coup_joueur1!= "pierre" and coup_joueur2 != "pierre" or coup_joueur1!= "feuille"  and coup_joueur2 != "feuille" or coup_joueur1!= "ciseaux" and coup_joueur2 != "ciseaux":
        continue
    elif coup_joueur1=="pierre":
        print("pierre-----VS---")
    elif coup_joueur1=="feuille":
        print("feuille-----VS---")
    else:
        print("ciseaux-----VS---")
        
        
    if coup_joueur2=="pierre":
        print("pierre-----VS---")
    elif coup_joueur2=="feuille":
        print("feuille-----VS---")
    else:
        print("ciseaux-----VS---")
        
    nbr_dev=random.randint(1, 3)
    if nbr_dev==1:
        coup_pc=="pierre"
        print("pierre")
    elif nbr_dev==2:
        coup_pc=="feuille"
        print("feuille")
    else:
        coup_pc=="ciseaux"
        print("ciseaux")
        
    if coup_joueur1==coup_joueur2 and coup_joueur2==coup_pc:
        print("egalité ! ")
        nul=nul+1
        
        
        
#   condition de gain du joueur 1  contre le joueur 2     
        
    elif coup_joueur1=="pierre" and coup_joueur2=="ciseaux" and coup_pc=="feuille":
        print(nom1, "vous avez gagné contre  !",nom2)
        user_victoire1=user_victoire1+1
        print(nom2, "vous avez perdu !")
        print("l'ordinateur a gagné contre !",nom2)
        pc_victoire=pc_victoire+1
    elif coup_joueur1=="feuille" and coup_joueur2=="pierre" and  coup_pc=="feuille":
        print(nom1, "vous avez gagné contre !",nom2)
        user_victoire1=user_victoire1+1
        print(nom2, "vous avez perdu !")
        print("l'ordinateur a gagné contre !",nom2)
        pc_victoire=pc_victoire+1
    elif coup_joueur1=="ciseaux" and coup_joueur2=="feuille"  and  coup_pc=="feuille":
        print(nom1, "vous avez gagné contre!",nom2)
        user_victoire1=user_victoire1+1
        print(nom2, "vous avez perdu !")
        print("l'ordinateur a gagné ccontre !",nom2 )
        pc_victoire=pc_victoire+1
    elif coup_joueur1=="ciseaux" and coup_joueur2=="pierre"  and  coup_pc=="feuille":
        print(nom1, "vous avez gagné contre !",nom2)
        user_victoire1=user_victoire1+1
        print(nom2, "vous avez perdu !")
        print("l'ordinateur a gagné ccontre !",nom2 )
        pc_victoire=pc_victoire+1
        
        #   condition de gain du joueur 2 contre le joueur 1
        
        
        
    elif coup_joueur2=="pierre" and coup_joueur1=="ciseaux":
        print(nom1, "vous avez perdu !")
        print(nom2, "vous avez gagné !")
        user_victoire2=user_victoire2+1
    elif coup_joueur2=="feuille" and coup_joueur1=="pierre":
        print(nom1, "vous avez gagné !")
        print(nom2, "vous avez perdu !")
        user_victoire2=user_victoire2+1
    elif coup_joueur2=="ciseaux" and coup_joueur1=="feuille":
        print(nom1, "vous avez gagné !")
        print(nom2, "vous avez perdu !")
        user_victoire2=user_victoire2+1
    elif coup_joueur2=="ciseaux" and coup_joueur1=="pierre":
        print(nom1, "vous avez gagné !")
        print(nom2, "vous avez perdu !")
        user_victoire2=user_victoire2+1
        
        # condition de gain de l'ordinateur face au joueur 1
        
    elif cou_pc=="pierre" and coup_joueur1=="ciseaux":
        print(nom1, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
    elif cou_pc=="feuille" and coup_joueur1=="pierre":
        print(nom1, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
    elif cou_pc=="ciseaux" and coup_joueur1=="feuille":
        print(nom1, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
    elif cou_pc=="ciseaux" and coup_joueur1=="pierre":
        print(nom1, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
        
            # condition de gain de l'ordinateur face au joueur 2     
        
    elif cou_pc=="pierre" and coup_joueur2=="ciseaux":
        print(nom2, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
    elif cou_pc=="feuille" and coup_joueur2=="pierre":
        print(nom2, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
    elif cou_pc=="ciseaux" and coup_joueur2=="feuille":
        print(nom2, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1
    elif cou_pc=="ciseaux" and coup_joueur2=="pierre":
        print(nom2, "vous avez perdu !")
        print( "l'ordinateur as gagné !")
        pc_victoire=pc_victoire+1       
