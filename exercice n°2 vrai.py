i=0
tab=[]
quest=int(input("combien d'entier aimerai vous entrer ? :"))
while i<quest:
    print("veuillez saisir le ", i+1," eme entier ")
    saisir=input()
    saisir=int(saisir)
    tab.append(saisir)
    i=i+1
    
h=0
p=0
grds=tab[0]
while h<len(tab):
    if grds>tab[h]:
        grds=grds
        p=0
    elif grds<tab[h]:
        grds=tab[h]
        p=tab[h]
    h=h+1 
    
    
t=0
u=0
pett=tab[0]
while t<len(tab):
    if pett<tab[t]:
        pett=pett
        u=tab[t]
        
    elif pett>tab[t]:
        pett=tab[t]
        u=tab[t]
        u=0
    t=t+1
    
    
    
    
    
    
    
posi=0
nega=0
a=0
c=-1
while a<len(tab):
    if tab[a]*c>0:
        nega=nega+1
    else:
        posi=posi+1
        
    a=a+1
print("les ",quest," entier saisir sont ",tab)
print("il y'a ",nega," entier negatifs")
print("il y'a ",posi," entier positif")
print("le plus grands est :",grds)
print("sa position est :",p)
print("le plus petit est ",pett)
print("sa position est :",u)
