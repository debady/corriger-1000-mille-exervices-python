import random
print()
nom=input("veuillez saisir votre nom sil vous : ")
print()
user_victoire=0
pc_victoire=0
nul=0
while True:
    print(nom ," : ",user_victoire,"points   /partie nul : ",nul," points  /victoire pc: ",pc_victoire,"points ")
    print()
    print("veuillez saisir votre coup entre :")
    print(" PIERRE")
    print("FEUILLE  ")
    print("CISEAUX ")
    print("ou QUITTER le jeu")
    print()
    coup_joueur=input("------->")
    if coup_joueur=="quitter":
        print("vous avez quitter le jeu !")
        break
    elif coup_joueur!="pierre" and coup_joueur!="ciseaux" and coup_joueur!="feuille":
        continue
    elif coup_joueur=="pierre":
        print("pierre--VS--" ,end=" ")
    elif coup_joueur=="feuille":
        print("feuille--VS--" ,end=" ")
    elif coup_joueur=="ciseaux":
        print("ciseaux--VS--" ,end=" ")
    nombre_randon=random.randint(1, 3)
    if nombre_randon==1:
        coup_pc="pierre"
        print(" pierre")
    elif nombre_randon==2:
        coup_pc="feuille"
        print(" feuille")
    elif nombre_randon==3:
        coup_pc="ciseaux"
        print(" ciseaux")
    
    if coup_joueur==coup_pc:
        nul=nul+1
    elif coup_joueur=="pierre" and coup_pc=="ciseaux":
        print("vous avez gagné !")
        user_victoire=user_victoire+1       
    elif coup_joueur=="feuille" and coup_pc=="pierre":
        print("vous avez gagné !")
        user_victoire=user_victoire+1  
    elif coup_joueur=="ciseaux" and coup_pc=="feuille":
        print("vous avez gagné !")
        user_victoire=user_victoire+1
        
        
        
    elif coup_joueur=="ciseaux" and coup_pc=="pierre":
        print("vous avez perdu !")
        pc_victoire=pc_victoire+1 
    elif coup_joueur=="pierre" and coup_pc=="feuille":
        print("vous avez perdu !")
        pc_victoire=pc_victoire+1 
    elif coup_joueur=="feuille" and coup_pc=="ciseaux":
        print("vous avez perdu !")
        pc_victoire=pc_victoire+1 
    elif coup_joueur=="pierre" and coup_pc=="ciseaux":
        print("vous avez perdu !")
        pc_victoire=pc_victoire+1 