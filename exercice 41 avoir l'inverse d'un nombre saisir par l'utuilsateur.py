n=int(input("veuillez saisir une valeurs :"))
inverse=0
m=n
while n!=0:
    inverse=(inverse*10)+(n%10)
    n=n//10
print("l'inverse de ", m,"est ",inverse)
