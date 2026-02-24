i=0
pg=0
somme=0

tab=[]
entier=int(input("combien dentier : "))
while i<entier:
    print("veuillez saisir le ",i+1," eme entier ")
    nbre=input()
    nbre=int(nbre)
    tab.append(nbre)
    somme=somme+nbre
  #  type(i)
    if tab[i]>i:
        pg=nbre
    elif pg>tab[i]:
        pg=pg
    elif pg<tab[i]:
        pg=tab[i]
    i=i+1   
print("la somme est ",somme)
print("le plus grand est ", pg)