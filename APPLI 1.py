print()

print("bienvenue sur GESTION DES MOYENNE DES ETUDIANTS")
print()

nom_direc=input("veuillez saisir votre nom : ")
print()

while True:
    
    nbre_matiere=input("combien de matiere ? ")
    nbre_matiere=int(nbre_matiere)
    print()
    a=0
    tab_matiere=[]
    
    
    while a<nbre_matiere:
        
        print("veuillez entrez la ",a+1, "em matiere svp ")
        nom_matiere=input()
        tab_matiere.append(nom_matiere)
        print()
        
        a=a+1
        
    
    nbre_etudiant=input("combien d'etudiants ? ")
    nbre_etudiant=int(nbre_etudiant)
    print()
    z=0
    tab_nom_etud=[]
    
    while z<nbre_etudiant:
        
        print("veuillez saisir le nom du ",z+1," eme etudiants")
        nom_etud=input()
        tab_nom_etud.append(nom_etud)
        print()
        
        z=z+1
    
        
        
    
    e=0
    while e<nbre_etudiant:
        
        
        print("saisisez la moyenne de ",tab_nom_etud[e])
        
        somme_moy=0
        b=0
        print()
        
        while b<nbre_matiere:
            
            
            print("en",tab_matiere[b])
            
            moy=input("entez : ")
            moy=int(moy)
            print()
            
            if moy>20:
                print("entrer une moyenne correct !")
                print()
                continue
            elif moy<0:
                print("entrez une moyenne correct svp !")
                print()
                continue
                
            print()
            
            somme_moy=somme_moy+moy
            b=b+1
        
        print("la moyenne generale de ",tab_nom_etud[e],"est : ",somme_moy/nbre_matiere)
        
        e=e+1
        

        
    break

