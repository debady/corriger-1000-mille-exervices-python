while True:
    
    age=int(input("veuillez saisir l'age de l'enfant : "))
    if age<=7 and age<=6 :   
        print("l'enfant est un POUSSIN !")
    elif age >=8 and age <=9:
      print("l'enfant est un pupilde !")
        
    elif age >=10 and age <=11:
      print("l'enfant est un minime !")
    elif age >12:
       print("l'enfant est un cadets !")
    demande =input("voulez continuer ? :")
    if demande=="non":
        print("vous avez quitter la partie ")
        break
