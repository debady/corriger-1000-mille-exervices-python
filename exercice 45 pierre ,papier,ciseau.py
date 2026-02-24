import random
print()
print()
nom=input("veullez saisir votre nom  :   ")
print("")
print("") 
    

    
    
user_victoire=0
pc_victoire=0
nul=0
while True:
    print()
    print(nom," :",user_victoire,"egalité :",nul,"victoire_pc:",pc_victoire ,":")
    print()
    print("choisisez un coup entre :PIERRE; FEUILLE, CISEAUX ,ou voulez vous quitter ? ")
    print()
    
    #print("ou voulez vous quiter le game ? ")
    

    coup_gamer=input("--->")
    print()
    if coup_gamer=="oui":
        print("vous avez quiter le game !")
        break
    if coup_gamer!="feuille" and  coup_gamer!="pierre" and  coup_gamer!="ciseaux":
        continue
    elif coup_gamer=="pierre":
        print("pierre---VS---",end=" ")
    elif coup_gamer=="feuille":
        print("feuille---VS---",end=" ")
    else:
        print("ciseaux---VS---",end=" ")
        
    randon_nombre=random.randint(1,3)
    
    if randon_nombre==1:
        coup_pc="pierre"
        print("pierre")
    elif randon_nombre==2:
        coup_pc="feuille"
        print("feuille")
    else:
        coup_pc="ciseaux"
        print("ciseaux")
        
        
    if coup_gamer==coup_pc:
        print("partie nul")
        nul=nul+1
        
        
        
    elif coup_gamer=="pierre" and coup_pc=="ciseaux" :
        print("vous avez perdu !")
    elif coup_gamer=="pierre" and coup_pc=="feuille":
        print("vous avez perdu !")
        pc_victoire=pc_victoire+1
    elif coup_gamer=="feuille" and coup_pc=="pierre":
        print("vous avez gagné !")
        user_victoire=user_victoire+1
    elif coup_gamer=="ciseaux" and coup_pc=="feuille":
        print("vous avez gagné !")
        user_victoire=user_victoire+1
    elif coup_gamer=="ciseaux" and coup_pc=="pierre":
        print("vous avez gagné !")
        user_victoire=user_victoire+1
    
    
    
    
    elif coup_pc=="pierre" and user_victoire=="ciseaux":
        print("vous avez perdu !")
        coup_pc=coup_pc+1
    elif coup_pc=="feuille" and user_victoire=="pierre":
        print("vous avez perdu !")
        coup_pc=coup_pc+1
    elif coup_pc=="ciseaux" and user_victoire=="feuille":
        print("vous avez perdu !")
        coup_pc=coup_pc+1
        
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

    
    
    
    
    
    






