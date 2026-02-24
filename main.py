# import random as rd 
# x = 1
# valmax = 0
# posigrd = 0
# tab = []

# while x<21:
#     print('Entrez le nombre  numéro ',x)
#     nbre = rd.randint(-1000,10001)
#     tab.append(nbre)
#     print(nbre)

    # if valmax<nbre:
    #     valmax=nbre
    #     posigrd = x
#     x=x+1
# for i in range(1,len(tab)):
#     if tab[i]>valmax:
#         valmax=tab[i]
#         posigrd = i
# print(tab)
# print(valmax,'', posigrd)
# tab = []

# valgrd = 0
# posigrd = 0

# for i in range(1,21):
#     print('Veuillez saisir le nombre numéro ', i)
#     nbre = rd.randint(-99999,99999)
# tablo.append(nbre)
#     print(nbre)

#     tab.append(nbre)
#     # int(input())
#     if nbre> valgrd :
#         valgrd = nbre
#         posigrd = i
# print(tab)
# print("le plus grand nombre saisir est ",valgrd,' sa position est ',posigrd)


# print('veuillez saisir le premier nombre ')
# nbre1 = rd.randint(-10,11)
# print(nbre1)
# #  int(input())

# print('veuillez saisir le deuxieme nombre ')
# nbre2 = rd.randint(-10,11)
# print(nbre2)
# #  int(input())


# if nbre1>0 and nbre2>0:
#     print("le produit de ces deux nombre est positif")

# if nbre1<0 and nbre2<0:
#     print("le produit de ces deux nombre est positif")

# if nbre1<0 and nbre2>0:
#     print("le produit de ces deux nombre est négatif")

# if nbre1>0 and nbre2<0:
#     print("le produit de ces deux nombre est négatif")

import random as rd 
tablo = []
for i in range(1,500):
    nbre1 = rd.randint(100,999)
    tablo.append(nbre1)
    # print(nbre1)

    nbre2 = rd.randint(100,999)
    tablo.append(nbre2)
    # print(nbre2)

    nbre3 = rd.randint(100,999)
    tablo.append(nbre3)
    # print(nbre3)

    nbre4 = rd.randint(100,999)
    tablo.append(nbre4)
    # print(nbre4)

    nbre5 = rd.randint(100,999)
    tablo.append(nbre5)
    # print(nbre5)

    nbre6 = rd.randint(100,999)
    tablo.append(nbre6)
    # print(nbre6)

    nbre7 = rd.randint(100,999)
    tablo.append(nbre6)
    # print(nbre7)

    nbre8 = rd.randint(100,999)
    tablo.append(nbre8)    
    # print(nbre8)

    print(tablo)
    print(len(tablo))