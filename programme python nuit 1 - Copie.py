print (" PROGRAMME DE CALCULATRICE 1")
a = float(input("veuilez saisir le premier un nombre: "))
opperateur = input("veullez saisir l opperateur ")
b = float(input("veuillez saisir le deuxieme nombre :"))
if opperateur == "+" :
    print ("a+b=" , a+b)
elif opperateur == "-" :
    print ("a-b=" , a-b )
elif opperateur == "**" :
        print ("la puissance de " , a ,"par " , b ," est " ,format(a**b ,".2f" ))
elif opperateur == "*" :
    print ("a*b=" , a*b )
elif opperateur == "/" :
    if b!=0 :
        print("a/b=" ,a/b)
    else :
        print ("desoler la division de" , a ," par " , b ," est impossible :")
else :
    print (" desoler l opperateur est inccorect : ")


