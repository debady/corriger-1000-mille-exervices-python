while True:
    
    print()
    print("-----------------FORMULAIRE DE RENSEIGNEMENT--------")
    print()
    nom=input("veuillez saisir votre nom s'il vous plait : ")
    prenom=input("veuillez saisir votre prenom s'il vous plait : ")
    print()
    age=int(input("veuillez saisir votre age s'il vous plait : "))
    matricule=int(input("veuillez saisir votre matricule s'il vous plait : "))
    date_naissance=int(input("veuillez saisir votre date_naissance s'il vous plait : "))
    lieu_naissance =input("veuillez saisir votre lieu_naissance s'il vous plait : ")
    nationalite=input("veuillez saisir votre nationalite s'il vous plait : ")
    niveau_etude=input("veuillez saisir votre niveau_etude s'il vous plait : ")
    etablissement=input("veuillez saisir votre etablissement s'il vous plait : ")
    print()
    print("-----------------partie des moyennes --------")
    print()
    francais=float(input("veuillez saisir la moyenne en francais: "))
    pc=float(input("veuillez saisir la moyenne en francais: "))
    maths=float(input("veuillez saisir la moyenne en maths : "))
    anglais =float(input("veuillez saisir la moyenne en anglais :"))
    philo=float(input("veuillez saisir la moyenne en philosophie: "))
    eps=float(input("veuillez saisir la moyenne en eps : "))
    art_pl=float(input("veuillez saisir la moyenne en art plastique : "))
    svt=float(input("veuillez saisir la moyenne en eps : "))
    hist_geo=float(input("veuillez saisir la moyenne en histoire geographie : "))
    conduit=float(input("veuillez saisir la moyenne en conduit : "))
    somme = francais*3+maths*4+pc*4+anglais*1+philo*2+eps*1+art_pl*1+svt*4+hist_geo*2+conduit*1
    moyenne=somme/23
    print(" nom               : ",nom)
    print(" prenom            : ",prenom)
    print(" age               : ",age," ans")
    print(" matricule         : ",matricule)
    print(" date_naissance    : ",date_naissance)
    print(" lieu_naissance    : ",lieu_naissance)
    print(" nationalite       : ",nationalite)
    print(" niveau_etude      : ",niveau_etude)
    print(" etablissement     : ",etablissement)
    print()
    print("la moyenne de monsieurs /madames ",nom, prenom ,"est ",format(moyenne,".2f"))
    print("avec la mention  ")
    print()
    if moyenne<10:
        print("mauvais travail ! REDOUBLE")
    elif moyenne>=10 and moyenne<=12:
        print(" assez bien ! ADMIS en classe felicitation .")
    elif moyenne>=13 and moyenne<=14:
        print("bien ! ADMIS en classe STANDARD ..felicitation.")
    elif moyenne>=15 and moyenne<=17:
        print(" tresz bien ! ADMIS en classe MOYEN .felicitation")
    elif moyenne>=18 and moyenne<=19:
        print("excellent ! ADMIS en classe SUPERIEUR .felicitation")
    elif moyenne>19:
        print("surdouer ! ADMIS en classe des EXCELLENT .felicitation")
    demande=input("voulez vous continuer ? :")
    if demande=="non":
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    