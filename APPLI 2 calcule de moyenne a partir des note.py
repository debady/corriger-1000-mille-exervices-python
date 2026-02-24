
nbre_matiere=input("combien de matiere ? : ")
nbre_matiere=int(nbre_matiere)



a=0
tab_nom_matiere=[]

while a<nbre_matiere:
    if a==0:
        print("veuillez saisir la premiere matiere")
    else:
        print("veuillez saisir la ",a+1,"eme matiere")
        
    nom_matiere=input()
    tab_nom_matiere.append(nom_matiere)
    
    
    a=a+1
    
z=0
