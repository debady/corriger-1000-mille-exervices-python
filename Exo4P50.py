print('veuillez saisir le nombre de nombre à saisir ')
nbreNombre = int(input('...:'))

tabl = []
mini =0
som=0

x=1
while x< nbreNombre+1:
    print('veuillez saisir la valeur ',x)
    val=int(input('..:'))

    tabl.append(val)
    som=som+val

    if x==0:
        mini=val
    else:
        if mini>val:
            mini=val
        else:
           val=val
    x=x+1

moy = som/nbreNombre
nbreSup =0

for i in range(0,len(tabl)):
    if tabl[i]<moy:
        nbreSup=nbreSup+1


print("1 | pour afficher la moyenne du tableau")
print("2 | pour afficher la plus pétite valeur")
print("3 | pour afficher le nombre de note supérieur à la moyenne et le pourcentage corespondant")
demande = int(input('...:'))

while demande != 1 and demande != 2 and demande != 3 :
    print('Erreur, veuillez réesayer !')
    demande = int(input('...:'))

if demande ==1:
    print("la moyenne est :",moy) 
elif demande ==2:
    print("la plus petite valeur est :",mini)        
elif demande==3:
    print("le nombre de note supérieur à la moyenne est :",nbreSup," le pourcentage corespondant est ",(moy)/nbreSup,"\n")

print("les éléments du tableau sont ",tabl)
print("las somme est :",som)

print("el minimum est :",mini)
print("le nombre de note supérieur est :",nbreSup)
print("L epourcentage :",moy/nbreSup)
