# -------------Exercice 5----------------------------
#
#Ecrivez un programme permettant, toujours sur le même principe, à l’utilisateur de saisir un 
#nombre déterminé de valeurs. Le programme, une fois la saisie terminée, renvoie la plus 
#grande valeur en précisant quelle position elle occupe dans le tableau. On prendra soin 
#d’effectuer la saisie dans un premier temps, et la recherche de la plus grande valeur du 
#tableau dans un second temps.


print("combien d' entier voulez vous saisir ? :")

a=input()
a=int(a)
i=0
c=[]
gr=0
while i<a:
    
    b=input("saisiez le {} nombre " .format(i+1))
    b=int(b)
    c.append(b)
    i=i+1    
gr=c[0]
h=0
cp=0
while cp <len(c):
    
        
    if gr>c[cp]:
            
        gr=gr
    else:
        gr=c[cp]
        h=cp
    cp+=1
print("la plus grande valeurs est {} et l'indice est {} ".format(gr,h))
