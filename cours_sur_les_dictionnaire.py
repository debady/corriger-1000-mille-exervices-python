# afficher le nombre de caractere  d'une valeurs et le nombre de caractere de sa chef 

b={}
b={'classe':'maths','nom':'jacque'}

# la varaible k a represente les valeurs et v represent les clef

for (k,v) in b.items():
    print(k," : a poour taille ",len(k)," et ",v," a pour taille ",len(v))
    
# stocker les donne entrer par un utulisateurs dns un dictionnaire 


print("veuillez saisir le nom de l'etudiants " )
nom= input()
print("veuillez saisir sa moyenne " )
note= int(input())
r={nom:note}

for (w,f) in r.items():
    print("le nom de l'etudiant est ",r.keys()," sa moyenne est ",note)
    # slicing permet de trancher des structure de donne
    
a=list(range(10,16))
# va compter de 10 a 16-1
a[1:5]
# commencer a l'indix 1 a l'indix max-1 qui est 5-1

a[0:3]
# commencer a l'indix 0 a l'indix max-1 qui est 3-1
# pour tout afficher 
a[0:6]
# porquoi 6 car il ne prends pas en comptes l'indix max du cout on fait l'indix max+1
# ou
a[:]
# indice negatif commmence de la fin au debut mais il n'y pas d'indice 0 du cout il commence a -1
a[-5]
a[2:-2]
# il va sauter deux indix de la droit vers la gauche et affivher le suivants ainsi de la droite vers la gauche
s=a[1:5:3]
s
[11, 14]
# 1 dans le crochet c'est lindix de departs et 2 cest le saute de nombre apres lindice suivants
# et le 6 represente le nombre des valeurs de la listes




# melanger les elements de deux liste
l=list(range(10,20))
l
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
t="ABCD"
t
'ABCD'
l[2:8]=t
l
[10, 11, 'A', 'B', 'C', 'D', 18, 19]
# on lui dit de la squance depart 2 a 5
# remplacer par les elements de t



mots=['jambon','fromage','continue','chocolat']
mots[2:2]=['miel']
mots
['jambon', 'fromage', 'miel', 'continue', 'chocolat']
# il compte de l droite vers la gauche 2 elemets et de l geuche vers la droit et inserer le mot


mots=['jambon','fromage','continue','chocolat']
mots[2:5]=[]
mots
['jambon', 'fromage']

# il prends les deux premier elements apres il replace par une liste vide



mots[1:]=['mayonnais','poulets','tomate']
mots
['jambon', 'mayonnais', 'poulets', 'tomate']
# il prends le premier elements et remplace le reste par la nouvelle liste 

