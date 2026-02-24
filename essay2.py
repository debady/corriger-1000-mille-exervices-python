import os 
os.getcwd()
os.chdir("c:\\modules_des_fichiers")
i=0
tab_nom_matiere=[]
nbre_matiere=int(input("veuillez saisir le nombre des matiere : "))
while i<nbre_matiere:
    print("veuillez saisir la",i+1," eme matiere ")
    nom_matiere=input()
    tab_nom_matiere.append(nom_matiere)
    
    b=open("pour_les_matieres.txt","a")  
    b.write(tab_nom_matiere[i])
    b.close()
    i=i+1
z=0 
tab_nom_etud=[]
nbre_etud=int(input("veuillz saisir le nombre des etudiants : "))
while z<nbre_etud:
    print("veuillez saisir le nom du",z+1," premier etudiants ")
    nom_etud=input()
    tab_nom_etud.append(nom_etud)
    b=open("pour_les_matieres.txt","a") 
    b.write("\n") 
    b.write(tab_nom_etud[z]+"\n")
    b.close()
    z=z+1
    
q=0
tab_moy_etud=[]
t=" "
while q<nbre_etud:
    print("veuillez saisir la moyenne de l'etudiant",tab_nom_etud[q])
    print("en ",tab_nom_matiere[q])
    moy=input()
    tab_moy_etud.append(moy)
    
    b=open("pour_les_matieres.txt","a")  
    b.write(tab_moy_etud[q])
    b.close()
    q=q+1
