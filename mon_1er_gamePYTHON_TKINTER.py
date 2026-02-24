import random

a=random.randint(0, 10)

poin_1=0
point2=0

nbre_essaie_1=4
nbre_essaie_2=4

nbre_essaie=5
s=1


nom_1=input("jouer 1 veuillez saisir votre nom :")
nom_2=input("jouer 2 veuillez saisir votre nom :")
print()



print("vous devrais devinez au bout de 4 essaies \br le bon nombre entre 0 et 10")
print()
print(nom_1,":",poin_1,' points ---',nom_2,":",point2,' points ',)
print()

while s<nbre_essaie:
    print(s," eme essaie")
    print()
    
    try:
        print(nom_1,'VOTRE NOMBRE :')
        devi_1=int(input())
        
        
    
        if devi_1>a:
            print("cest moins de sa ! ")
        elif devi_1<a:
            print("cest plus que sa ! ")   
        elif devi_1==a:
            poin_1=poin_1+1
            print('bravo',nom_1,' vous gagne ',poin_1,' point au ',s, "eme essaie")  
            quest=input('une autre partie  ? : ')
            if quest=='non' or quest=='no':
                break
            else:
                continue
     
    except ValueError:
        print('entrer un nombre raisonnable ')
        continue

    try:
        
        print(nom_2,'VOTRE NOMBRE :')
        devi_2=int(input())
        
    
        if devi_2>a:
            print("cest moins de sa ! ")
        elif devi_2<a:
            print("cest plus que sa :!")
        elif devi_2==a:
            point2=point2+1
            print('bravo',nom_2,' vous gagne ',point2,' point au ',s, "eme essaie")
            quest=input('une autre partie  ? : ')
            if quest=='non' or quest=='no':
                break
            else:
                continue
    
    except ValueError:
        print('veuillez saisir un nombre raisonnable')
        continue
    print()

    
        
            
    
    
    
    if s==4:
        print("vous avez epuisé les 4 essais setais",a)
        break
    
    
    
        
    
        

    s=s+1
    
    