conb=int(input("combien"))
tab=[]
import random
l=[i for i in range(1,conb+1)]
random.shuffle(l)
l.sort()
print(l)
print(len(l))
a=0
while a<len(l):
    tab.append(l)
    print(tab[a+1])
    a=a+1
    
import random
l=[i for i in range(1,nbre_joueur)]
random.shuffle(l)
l.sort()
m=0 
while m<nbre_joueur:
    tab[m]=l[m]
    m=m+1
    print(tab,end=" ")