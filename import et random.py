import random
nbre=random.randint(1, 7)
chance=0
if nbre==1:
    chance=="lundi"
elif nbre==2:
    chance=="mardi"
elif nbre==3:
    chance=="mercredi"
elif nbre==4:
    chance=="jeudi"
elif nbre==5:
    chance=="vendredi"
elif nbre==6:
    chance=="samedi" 
else:
    chance=="dimanche"
    
jour=0
nbre_tentativess=4
    
while jour< nbre_tentativess:
    print("veuillez saisir un jour de la semaines ")
    esay=input()
    if esay==nbre:
        print("bravo vous avez gagné ")
    else:
        print("houp!! ,vous vez perdu ! ")
        if nbre_tentativess!=0:
           print("c'etais",nbre)
        else:
            break
    jour=jour+1    
    