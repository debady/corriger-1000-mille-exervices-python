while True:
    try:
        nbre_copie = int(input("combien de copie : "))
        if nbre_copie<0:
            print("veuillez saisir un nmbre raisonnable ")
            continue
        
        elif 1<=nbre_copie<=10:
            prix=nbre_copie*25
            print("vous serai facturé à ",prix," FCFA")
            
        elif 11>=nbre_copie<=20:           
            prix=(10*25)+((nbre_copie-10)*20)          
            print("vous serai facturé à ",prix," FCFA")
            
        elif nbre_copie>20:
            prix=10*25+((nbre_copie-10)*20)+((nbre_copie-30)*10)
            print("vous serai facturé à ",prix," FCFA")
            
        
    except ValueError:
        print("le minimun est une 1 page svp: ")
        continue
    finally:
        quest =input("vous avez des copie a tirées ? : ")
        if quest =="oui" or quest =="yes":
            continue
            
        else:
            break
            
            