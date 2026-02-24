while True:
    
    print()
    print()
    print("CALCUATRICE CLASSIQUE" )
    print()
    print()
    print("---------------------MENU-------------")
    print()
    print()
    print(" 1 -----> pour l'addition ")
    print(" 2 -----> pour la soustraction ")
    print(" 3 -----> pour la division entier ")
    print(" 4 -----> pour multiplication ")
    print(" 5 -----> pour la puissance ")
    print(" 6 -----> pour la racine carré ")
    
    question =input("quel oppertion aimerez vous effectuer ?  :")
    
    if question=="1":
        terme1=int(input("veuillez saisir le premier terme :"))
        terme2=int(input("veuillez saisir le deuxieme  terme :"))
        print(" la somme de ", terme1,"et", terme2,"est egale a ", terme1+terme2)
        
        
    elif question=="2":
        terme1=int(input("veuillez saisir le premier terme :"))
        terme2=int(input("veuillez saisir le deuxieme  terme :"))
        print(" la soustraction de ", terme1,"et", terme2,"est egale a ", terme1-terme2)
        
    elif question=="4":
        terme1=int(input("veuillez saisir le premier terme :"))
        terme2=int(input("veuillez saisir le deuxieme  terme :"))
        print(" la multiplication de ", terme1,"par", terme2,"est egale a ", terme1*terme2)
        
    elif question=="5":
        terme1=int(input("veuillez saisir le premier terme :"))
        terme2=int(input("veuillez saisir le deuxieme  terme :"))
        print(terme1," puissance  ", terme2,"est egale a ", terme1**terme2)
        
    elif question=="3":
        terme1=int(input("veuillez saisir le premier terme :"))
        terme2=int(input("veuillez saisir le deuxieme  terme :"))
        if terme2!=0:
            print(" la division de ", terme1,"par", terme2,"est egale a ", terme1/terme2)
        else:
            print("desolé la division de ",terme1,"par",terme2,"est impossible !")
    demande=input("voulez vous effectuer d'autre oppration ? ")
    if demande=="non":
        break 
            
        
        
        
