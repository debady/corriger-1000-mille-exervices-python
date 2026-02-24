nbre_ligne=int(input('veuillez saisir le nbre de ligne : '))
n=11606 
for i in range(1,nbre_ligne+1):
    for j in range(1,nbre_ligne-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(chr(n),end=" ")
        n=n+1
    print()
    
        