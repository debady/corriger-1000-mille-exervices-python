def nbrpattes(poulet,vache,chevaux,oies):
   # f=poulet*2+vache*4+chevaux*4+oies*2
    # ou 
    p=poulet*2
    v=vache*4
    c=chevaux*4
    o=oies*2 
    sp=p+v+c+o
    return sp
poulet=int(input("veuillez saisir le nombre de poulets : "))
vache=int(input("veuillez saisir le nombre de vaches : "))
chevaux=int(input("veuillez saisir le nombre de chevaux : "))
oies=int(input("veuillez saisir le nombre de oies : "))
somme=nbrpattes(poulet, vache, chevaux, oies)
print("le nombre de pattes des animaux est ",somme,"pattes")

