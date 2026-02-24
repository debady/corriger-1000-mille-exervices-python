def prix(km):
    k=km
    cout_L=695
    litre=km/100
    pay=litre*cout_L
    return pay
k=int(input("veuillez saisir la distances a aprcourir : "))
v=prix(km)
print("vous payerais ",v," FCFA")
