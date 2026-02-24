
          
                          # question 1
  
import math
a=float(input("veuillez saisir un nimbres flottants : "))
c=-1
if a*c<0 or a==0:
    print("la racines carré de ",a," est",math.sqrt(a))
else:
    print("erreur")
    
                 # question 2
                 
saisir1=input("veuillez saisir le premier mots : ")
saisir2=input("veuillez saisir le deuxieme mots : ")
if saisir1<saisir2:
    print("le plus petit est ",saisir1)
elif saisir1==saisir2:
    print("egalité",saisir1," et",saisir2)
else:
    print("le plus petit est ",saisir2)
    
                     # question 3
pSeuil=2.3
vSeuil=7.41
while True:
    pres=float(input("veuillez saisir la pression de l'enceint : "))
    vol=float(input("veuillez saisir le volume de l'enceint : "))
    if pres>pSeuil and vol>vSeuil:
        print("arret immediat")
    elif pres>pSeuil:
        print("augmenter le volume de l'enceint ! ")
    elif vol>vSeuil:
        print("diminuer le volume de l'enceint ! ")
    else:
        print("tout va bien ! ")
        
        # question 4
        
        
a=0
b=10
print("les valeurs de a tant que a est inferieur a b sont \n :")
while a<b:
    print(a,end=" ")
    a=a+1
print("les entier pair de b sont : ",b,end=" ")
while b>0:
    if b%2==0:
        print(b)
    b=b-1


           # question 4
           
           
for i in range(1,11):
    print("veuillez saisie le ",i, " eme entier")
    a=input()
    a=int(a)
    print(a)
    
    
# question 5

print("exemple 1" .center(40,'-'))
for lettre in "cia":
    print(lettre)
print()