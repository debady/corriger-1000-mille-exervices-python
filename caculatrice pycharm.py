print("CACULATRICE DE TOUT LES OPERTION")
nbr1 = int(input("veuillez saisir le premier terme : "))
operateur = input ("veuiller saisir l operateur ")
nbr2 = int(input("veuillez saisir le deuxieme terme :"))
if operateur == "+":
    print(nbr1+nbr2 )
elif operateur == "-":
        print(nbr1 - nbr2)
elif operateur == "*":
        print(nbr1 *nbr2)
elif operateur == "/":
    if nbr2 < 1:
        print("la division de " , nbr1 , "par" , nbr2 ," est impossible. ")
    else :
        print(nbr1 /nbr2)

elif operateur == "**":
        print(nbr1 ** nbr2)
else :
    print (" l operateur est inccorect ")
print("l addition de " ,nbr1 , "et" , nbr2 ,"est egale a " ,format(nbr1+nbr2, ".2f" ))
print("la soustration de " ,nbr1 , "par" , nbr2 ,"est egale a " ,format(nbr1-nbr2, ".2f" ))
print("la multiplication " ,nbr1 , "par" , nbr2 ,"est egale a " ,format(nbr1*nbr2, ".2f" ))
print("la divion de " ,nbr1 , "par" , nbr2 ,"est egale a " ,format(nbr1/nbr2, ".2f" ))
print("la puissance de " ,nbr1 , "puissance" , nbr2 ,"est egale a " ,format(nbr1/nbr2, ".2f" ))