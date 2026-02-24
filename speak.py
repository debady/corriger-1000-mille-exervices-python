pwd1 =input('veuillez saisir votre psswdd :')
#pwd2 =input('veuillez saisir votre psswdd :')

tab=[]
tab.append(pwd1)


while True:
    if len(tab[0]) <4:
        print("le psswd doit contenir au moins 4 caractere ")
        pwd1 =int(input())
        continue

    else:
        print('valide !')
        break