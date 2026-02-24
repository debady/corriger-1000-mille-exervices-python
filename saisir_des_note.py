import os 

os.getcwd()

os.chdir("C:\1_PROGRAMME_PYTHON\_PROGRAMME_")

nbre_matiere=int(input("combien de matiere ? :"))

i=0

tab=[]

while i<nbre_matiere:

    if i<1 and i>=1:

        print("veuillez saisir la 1 ere matiere")
    else:

        print("veuillez saisir la ",i+1," eme matiere")
    matiere=input()

    tab.append(matiere)

    i=i+1

a=0
tab_nom_etud=[]
nbre_etud=int(input("combien d'etudiants ? :"))
while a<nbre_etud:
    if i==1:
       print("veuillez saisir le nom du premier ere etudiants")
    else:
        print("veuillez saisir le nom du ",a+1," eme etudiants")
    nom_etud=input()
    tab_nom_etud.append(nom_etud)
    a=a+1
tab_moy_des_etudt=[]  
n=0
while n < nbre_etud and n<nbre_matiere:
    print("veuillez saisir la moyenne en",tab[n],"de ",tab_nom_etud[n])
    moyen_etud=input()
    tab_moy_des_etudt.append(moyen_etud)
    n=n+1
    break 


while True:
    if nbre_etud>len(nbre_matiere):
        s=0
        while s<nbre_etud:
            print(tab_nom_etud[s]," : ",tab_moy_des_etudt[s] ,"en ",tab[s])
            a=open("samedi.txt","a")
            a.write("\n"+tab_nom_etud[s]+" : "+tab_moy_des_etudt[s] +" : "+tab[s]+"\n")
            a.close()
            nbre_etud=nbre_etud-1
    else:
        t=0
        while t<len(nbre_matiere):
            print(tab_nom_etud[s]," : ",tab_moy_des_etudt[s] ,"en ",tab[s])
            a=open("samedi.txt","a")
            a.write("\n"+tab_nom_etud[s]+" : "+tab_moy_des_etudt[s] +" : "+tab[s]+"\n")
            a.close()
            t=t+1