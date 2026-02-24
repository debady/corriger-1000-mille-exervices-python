n=int(input("veuillez saisir une valeurs :"))
inverse=0
m=n
while n!=0:
    inverse=(inverse*10)+(n%10)
    n=n//10
print("linverse de ", m,"est ",inverse)
if inverse==m:
    print("et est un palindromme ")
else:
    print("et n'set pas un palindromme ")