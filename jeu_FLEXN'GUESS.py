i=0
tab=[]
nbre_joueur=int(input("combien de personne participent au jeu ? :"))
while i<nbre_joueur:
    print("veuillez saisir le nom  du",i+1, " eme joueur ")
    nom=input()
    tab.append(nom)
    i=i+1
a=0
while a<len(tab):
    print(a+1, " eme joueur :",tab[a])
    a=a+1
print("combien de personne eliminerai vous a la fin de la premiere manche ? ")
tab_nbre_a_elim=[]
while True:
    nbre_elim=input()
    nbre_elim=int(nbre_elim)
    if nbre_elim>=nbre_joueur:
        print("desolé le nombre de personne a eliminé  ne doit pas depasé ou etre egale au nombre de joueur ")
        print("entre a nouveau !")
        continue
    elif nbre_elim<nbre_joueur:
        tab_nbre_a_elim.append(nbre_elim)
        if tab_nbre_a_elim[0]==1 :
            print("la  derniere personnes seront eliminés a la fin de la premiere manche ")
            break
        else:
            print("les",nbre_elim,"  derniere personnes seront eliminés a la fin de la premiere manche ")
            break
a=0
m=0
while a<nbre_joueur:
    import random
    l=[i for i in range(1,nbre_joueur)]
    random.shuffle(l)
    l.sort()
    print(tab[a]," quel est la racine carré de 25 ")
    quest1=input()
    quest1=int(quest1)
    if quest1==5:
        print("tres bien ")  
    else:
        print("mauvaise reponse !")     
    print(tab[a]," quel est la capitale de la france ?  ")
    quest2=input()
    if quest2=="paris":
        print("tres bien ")
    else:
        print("mauvaise reponse !")
        break
        print(tab[a],"vous avez + ",l[m]," points")
    a=a+1
    m=m+1

