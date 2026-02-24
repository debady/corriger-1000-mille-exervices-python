while True:
    import os
    os.getcwd()
    os.chdir("c:\\mes_application_solo")
    print("veuillez saisir votre nom ")
    nom_educ=input()
      
    tab_nom_matiere=[]
    a=0
    nbre_matiere=int(input("combien dematiere : "))
    
    while a < nbre_matiere:
        
        print("veuillez saisir ",a+1, " eme matiere")
        nom_matiere=input()
        tab_nom_matiere.append(nom_matiere)
        
        open("nom_des_matiere.txt","a")
        b=open("nom_des_matiere.txt","a")
        b.write(nom_matiere+"\n")
        b.close()
        
        a=a+1
    
    
    nbre_etudiante=int(input("combien d'etudiants : "))
    
    z=0
    
    while z<len(tab_nom_matiere):
        print("en")
        print(tab_nom_matiere[z],"combiend de note ")
        nbre_note=int(input())
        
        z=z+1
        
