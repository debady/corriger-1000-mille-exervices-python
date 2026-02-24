while True:
    n=int(input("veuillez saisir un nombres : "))
    if n*(-1)>0:
        print(n,"est un nombres negatif ")
    elif n*(-1)<0:
        print(n,"est un nombres positif ")
    else:
        print("0 est neutre")