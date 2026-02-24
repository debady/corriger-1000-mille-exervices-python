while True:
    mot_pass = input('MOT DE PASSE : ')

    nom=input("NOM  : ")
    prenom=input('PRENOM :')
    
    x=0
    tab=[]  
    nbre_matiere=int(input("NOMBRE DE MATIERE : "))
    while x<nbre_matiere:
        print(x+1," EME MATIERE : ")
        matiere=input()
        tab.append(matiere)
        x=x+1
    
    a=0
    somme=0
    while a<len(tab):
        print('NOTE EN ',tab[a])
        note=float(input('------> : '))
        somme=somme+note
        a=a+1
    moy = somme/nbre_matiere
    mention=''
    dec=''
    
    if moy<10:
        mention=='MAUVAIS TRAVAIL '
    elif 10>=moy<=12:
        mention=='passable '
        dec='DOUBLE'
    elif 13>=moy<=15:
        mention=='bien'
        dec='ADMIN'
    elif 16>=moy<=18:
        mention=='tres bien'
        dec='ADMIN TABLEAU DHONNEUR'
    elif moy>18:
        mention=='EXCELLENT'
        dec='CLASSE SPECIALE !'
    revio =input("REBIS MOT DE PASSE : ")    
    
    while revio !=mot_pass:
        print('mot de passe incorrect !')
        mot_pass=input()
        continuem

        
    print('NOM : ',nom)
    print('PRENOM : ',prenom)
    print("MOYENNE : ",moy)
    print("DELIBERATION : ",dec)
    print("MENTION : ",mention)