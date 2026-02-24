i=0
tab_nom_joueur=[]
nbre_joueur=int(input("combien de personnes participes au jeu ? :"))
while i<nbre_joueur:
    print("veuilez saisir le nom du ",i+1," eme joueur ")
    nom_joueur=input()
    tab_nom_joueur.append(nom_joueur)
    i=i+1
a=0
tab_reponse=[]
while a<nbre_joueur:
    print("que y'a il entre le ciels et la terre ? ")
    print(tab_nom_joueur[a],"entrez votre reponse :")
    reponse=input()
    tab_reponse.append(reponse)
    if tab_reponse[a]=="et":
        print("bravo !",tab_nom_joueur[a],"vous avez trouvez : + ",a+1,"points")
        
    else:
        print("mauvaise reponse ! c'etais [et]")
    a=a+1

    

