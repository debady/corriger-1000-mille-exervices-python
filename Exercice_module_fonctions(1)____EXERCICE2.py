#------------------------------Exercice 2 ------------------------------

#           Ecrire un programme Python qui demande à l’utilisateur le nombre d’entier qu’il souhaite 
#           saisir, puis permet la saisie des entiers et effectue le tri dans l’ordre croissant des entiers 
#           saisis. Les valeurs sont à stocker dans une liste Python. L’utilisation des fonctions est 
#           fortement recommandée.


print()




a=0

print("combien d'entier voulez vous saisir ? :")


entier=input()
entier=int(entier )
while a<entier :
    
    print("veullez saisir le ",a+1," eme valeurs : ")
    valeurs=input()
    valeurs=int()
    tableau=[]
    tableau.append(valeurs)

    a=a+1
c=tableau
print(sorted(c))
