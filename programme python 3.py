print("PROGRAMME DE CALCUL DE MOYENNE ")
nom = input(" veuillez entrer le nom de l etudiant :")
prenom = input("veuillez saisir le prenom de l  etudiant :")
age = int(input("veuilez saisir l age de l eudiant :"))
matricule = input("veuillez saisir le matricule de l etudiant : ")
print(" le nom et prenom de l etudiant est ", nom , prenom , " de matricule " , matricule ,"de age" , age , "ans " )

moyenne_francais = float( input (" vuillez saisir la moyenne de francais :"))
moyenne_pc =float( input (" vuillez saisir la moyenne de phusique et chimie :"))
moyenne_art =float( input (" vuillez saisir la moyenne d art plastique :"))
moyenne_angl = float( input (" vuillez saisir la moyenne d anglais :"))



s = moyenne_francais + moyenne_pc + moyenne_art + moyenne_angl
d = s / 4

print("la moyenne est " , d)

if d < 10 :
        print (" avec la mention mauvais redouble :")
elif d >= 10 and d <= 12 :
        print(" avec la mention passable , et est admis en classe superieur :")
elif d >= 13 and d <= 15 :
            print(" avec la mention assez bien , et est admis en classe superieur :")
elif d >= 16 and d <= 17 :
        print(" avec la mention bien , et est admis en classe superieur :")
elif d >= 18 and d <= 19 :
        print(" avec la mention tres biene , et est admis en classe superieur :")
elif d >= 19 and d <= 20 :
            print(" avec la mention excellent , et est admis en classe superieur :")
elif d >=21 :
        print("super douher orienter a ESATIC :")
else :
        print("orienter")