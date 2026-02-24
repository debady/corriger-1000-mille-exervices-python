#-------------------------Exercice 1 ----------------------

#    votre programme doit tirer un nombre au hasard entre 100 et 500 et vous avez 10 (dix) essais 
#    pour le trouver. Après chaque tentative, l'ordinateur vous dira si le nombre que vous avez 
#    proposé est trop grand, trop petit, ou si vous avez trouvé le bon nombre.
#    Veuillez utiliser le module random (lire la doc du module) de python pour générer 
#    automatiquement l’entier à deviner.
#





import random
n=random.randint(100, 500)
nombre_tentative=10
m=nombre_tentative

print()

print(" l'ordinateur a choisir un nombre au hazard entre 100 et 500 , a vous de le deviner en 10 essaies .BONNE CHANCE !!!!")
print()
print()
while nombre_tentative>0:
    
    var =int(input("veuillez saisir votre chiffre deviné:" ))
    if var<n:
        print("c'est trop petit !")
        
    elif var>n:
        print("c'est trop grands ! ") 
    else:
        break
    nombre_tentative=nombre_tentative-1
if nombre_tentative!=0:
    print("bravo ! vous avez trouvez ",var,"au ",10-nombre_tentative,"eme essasie")
else:
    print("houps ! vous n'avez pas trouver. vous avez depasser les ",m,"tentative c'etait",n)

        
import random

x=random.randint(10, 500)

nbre_essaie=10
a=0
print("VOUD DEVEZ DEVINEE AU BOUT DE 10 ESSAIE LE BON NOMBRE ENTRE 100 ET  500".center(20,"*"))
while nbre_essaie>0:
    print(a+1," eme essaie ")
    print()
    print("votre nmbre devinez : ")
    coup_gamer=int(input())
    print()
    if coup_gamer>x:
        print("cest moins de ",coup_gamer)
    elif coup_gamer<x:
        print("cest plus que  ",coup_gamer)
    else:
        break
    nbre_essaie=nbre_essaie-1
    a=a+1
if nbre_essaie!=0:
    print("bravo vous avez trouvez au ",10-nbre_essaie," eme essaie ")
else:
    print("oup vous avez epuiseé les 10 essaie cetait ",x)

    