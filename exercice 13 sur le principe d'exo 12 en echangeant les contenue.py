a=float(input("veuillez saisir la valeur de A : "))
b=float(input("veuillez saisir la valeur de B : "))
if a*b>0:
    a,b=b,a
    print("comme ",a,"et ", b, "ont le meme signe alors ,la nouvelle valeurs de A est ",a,"et la nouvelle valeurs de B est ",b)
else:
    somme = a+b
    prod=a*b
    print("la somme de ", a,"et ", b,"est egale a ", somme)
    print("la produit de ", a,"et ", b,"est egale a ", prod)

    