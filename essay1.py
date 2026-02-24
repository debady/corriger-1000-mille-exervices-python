import os
os.getcwd()
os.chdir("c:\\modules_des_fichiers")
i=0
nbre_etud=int(input("combien d'etudiants ? :"))
while i<nbre_etud:
    print("veuillez saisir le nom du ",i+1," eme etudiants ")
    nom_etud=input()
    print("veuillez saisir sa note")
    note_etud=input()
    affiche=nom_etud+" : "+note_etud
    
    a=open("mon_text1.txt","a")
    a.write(affiche)
    a.close()
    print(affiche ,end="\n")
    i=i+1