a=input("combien d'entier voulez vous saisir ? :")
a=int(a)
i=0
c=[]
gr=0
while i < a :
    b=input("saisisez le {} nombre ".format(i+1))
    b=int(b)
    c.append(b)
    i=i+1
    gr=c[0]
    h=0
    cp=0
    while cp<len(c):
        if gr>c[cp]:
            gr=gr
        else:
            gr=c[cp]
            h=cp
        cp+=1
print("la plus grande valeurs est {} et l'indice est {} ".format(gr,h))