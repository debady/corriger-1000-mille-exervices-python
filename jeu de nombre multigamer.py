i=0
tab_nom_joueur=[]
nbre_joueur=int(input("combien de particiapnts ?  : "))

while i<nbre_joueur:
    print("veuillez saisir le nom du ", i+1 ," JOUEUR")
    
    nom_joueurs=input()
    tab_nom_joueur.append(nom_joueurs)
    
    import os
    os.getcwd()
    os.chdir("c:\\mes game_jeux")
    
    open("nom_des_joueurs.txt","a")
    a=open("nom_des_joueurs.txt","a")
    a.write("                       LISTES DES JOUEURS                    "+":\n")

    a.write(tab_nom_joueur[i]+":\n")
    a.write(":\n")

    
    a.close()

    i=i+1
    


while True:
    nbre_joueur_a_eliminer=int(input("ROUND 1 combien de personnes a eliminées ? :"))
    if nbre_joueur_a_eliminer>=1 and nbre_joueur_a_eliminer<nbre_joueur:
        x=nbre_joueur_a_eliminer 
        if nbre_joueur_a_eliminer==1:
            print("le dernier ou la derniere sera éliminée ! ")
        else:
            print("les", x," dernieres personnes seront éliminée !")
        break
    elif nbre_joueur_a_eliminer>=nbre_joueur:
        print("desolé le nombre ne doit pas etre egale ou depassé le nombre de joueur ! ") 
        print("veuillez reesayé ! ")
        continue
    elif nbre_joueur_a_eliminer==0:
        print("desolé le nombre doit etre superieur ou egal a 1 ")
        print("veuillez reesayé ! ")
        continue
tab_couleur_joueur=[]
a=0
x=0
liste="                       LISTES DES JOUEURS                   "  
liste1="                      CHOIX DES COULEURS DES JOUEURS                      " 

while a<nbre_joueur:
    print(tab_nom_joueur[a],"quelle est votre couleur ? ")
    couleur_joueur=input()
    tab_couleur_joueur.append(couleur_joueur)
    
    
    import os
    os.getcwd()
    os.chdir("c:\\mes game_jeux")
    a.write(liste+"\n")

    
    open("couleur_joueur.txt","a")
    a=open("couleur_joueur.txt","a")

    a.write(tab_nom_joueur[i]+" : "+tab_couleur_joueur[a]+":\n")
    a.write(":\n")

    
    a.close()

    a=a+1