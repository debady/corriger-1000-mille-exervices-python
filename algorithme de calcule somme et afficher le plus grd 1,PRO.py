print("demander a l utulisateur combien de nombre il aimerait calculer ensuite additionner tout les nmbre quil a entrer ensuit afficher le plus grand. ")
print()
print()
# on va mettre tout les entier a (0)
PG=0
nbre=0
i=0
somme=0


a=int(input("combien d entier voulez vous saisir ? :"))
while i<a:
    print("entrer l'entier ", i+1 ,":")
    nbre=input()
    nbre=int(nbre)
    somme=somme+nbre
    type(i)
    
    if i==0:
        PG=nbre
        #print(PG)
    elif PG>nbre:
        PG=PG
    else:
        PG=nbre
    i=i+1
print("la somme est ",somme)
print("et le plus grand est",PG)