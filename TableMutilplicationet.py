#-----------------
# ECRIRE UN PROGRAMME QUI AFFICHE LA TABLE DE MULTIPLICATION 
#-----------------

depart1 = 1
while depart1<10:
    print('\ntable de ',depart1)
    depart2 = 1
    while depart2 <10:
        print(depart1,'*',depart2,'=',depart1*depart2)
        depart2+=1
    depart1+=1