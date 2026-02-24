nbr=int(input("veuillez saisir un nombre : "))
fact=1
for i in range(1,nbr+1):
    fact=fact*i
    print(fact*i)
print(nbr,'!=',fact)