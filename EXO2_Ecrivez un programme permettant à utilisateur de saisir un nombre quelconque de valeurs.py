print("combien de valeurs comptez vous saisir ?  :")
question =int(input())

nbre_valeurs=question
i=0
verifit=-1
positif=0
negatif=0

while i<question:
    nbre_valeurs=nbre_valeurs-1
    print("saisisez la valeurs du ",i+1," eme nombre")
    valeurs=int()
    valeurs=input()
    i=i+1
    while verifit*i>0:
        positif=positif+1
    while verifit*i<0:
        negatif=negatif+1
        print(positif)
        print(negatif)
        i=i+1
    i=i+1