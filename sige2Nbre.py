nbre1 = int(input('veuillez saisir le premier nbre :'))
nbre2 = int(input('veuillez saisir le deuxieme nbre :'))

if (nbre1*nbre2>0):
    print(nbre1," et ", nbre2, " sont de meme signe")
else:
    if nbre1*(-1)>1:
        print(nbre1 ," est le premier nbre et est negatif")
    if nbre2*(-1)>1:
        print(nbre2 ," est le deuxieme nbre et est negatif negatif")

    if nbre1*(-1)<1:
        print(nbre1 ," est le premier nbre et est positif")
    if nbre2*(-1)<1:
        print(nbre2 ," est le deuxieme nbre et est positif")