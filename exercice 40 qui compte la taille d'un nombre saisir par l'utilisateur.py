n=int(input("veuillez saisir une valeurs quelquonc :"))
m=n
nbr=0
while n!=0:
    n=n//10
    nbr=nbr+1
print("le nombre de chiffre de la valeurs ", m,"est ",nbr)