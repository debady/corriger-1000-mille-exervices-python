while True:
    
    import math
    from math import sqrt
    
    nbre1=int(input("veuillez saisir le premiere nombre : "))
    op=input("veuillez saisir l'operateur : ")
    nbre2=int(input("veuillez saisir le premiere nombre : "))
    
    
    raci_nbre2= math.sqrt(nbre1)
    raci_nbre1= math.sqrt(nbre1)
    
    div=nbre1+nbre2
    sous=nbre1-nbre2
    
    mult=nbre1*nbre2
    somme=nbre1+nbre2
    puis=nbre1**nbre2
    
    if nbre2== "0" and op== " / ":
        print("la division par zero est impossible .veuillez saisir a nouveau ")
        continue
    else:
        rest_div=nbre1%nbre2
        quo_div=nbre1 //nbre2
        div=nbre1/nbre2
        

        
    print(nbre1," + ", nbre2," = ",somme)
    print(nbre1," - ", nbre2," = ",sous)
    print(nbre1," / ", nbre2," = ",div)
    print(nbre1," * ", nbre2," = ",mult)
    print(nbre1," ** ", nbre2," = ",puis)
    print(nbre1," // ", nbre2," = ",quo_div)
    print(nbre1," % ", nbre2," = ",rest_div)
    
    quest=input("voulez vous continuer ? : ")
    
    if quest=="non" or quest =="no":
        break
