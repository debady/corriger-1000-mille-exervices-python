import random as rd 
tablo = []

nbreEntier  = rd.randint(10,50)
for i in range(nbreEntier):

    entier = rd.randint(0,500)
    tablo.append(entier)

print(tablo)

for j in range(0,nbreEntier):
    for i in range(j,nbreEntier):
        if tablo[i]<tablo[j]:
            resp = tablo[i]
            tablo[i]=tablo[j]
            tablo[j] = resp
print(tablo)



# import random as rd 
# tableau = []

# for i in range(5):
#     print("veuillez saisir ",i+1," est élément")
#     entier=rd.randint(-9999,9999)
#     tableau.append(entier)
# print("valeur du tableau sont ",tableau)

# i=0
# j=4
# print()
# plusgrand = tableau[0]
# postgrd =1
# plusPtt = tableau[4]
# positppt=1
# while i<=j:
#     resp = tableau[i]
#     tableau[i]=tableau[j]
#     tableau[j]=resp

#     if tableau[i]>plusgrand:
#         plusgrand=tableau[i]
#         postgrd=postgrd+1
#     if tableau[j]<plusPtt:
#         plusPtt=tableau[j]
#         positppt=positppt+1
#     i=i+1
#     j=j-1

# print("le contenue du tableau inversé est ",tableau)
# print("la plus grande valeur est ",plusgrand,' se trouve à la position ',postgrd)
# print("la plus pétite valeur est ",plusPtt,' se trouve à la position ',positppt)

import random as rd 
tablrao = []
for i in range(5):
    entier = rd.randint(-48555,885895)
    tablrao.append(entier)

print('les valeurs du tableau est ',tablrao)

i = 0
j=len(tablrao)-1

while i<=j:
    resp = tablrao[i]
    tablrao[i]=tablrao[j]
    tablrao[j]=resp

    # if tablrao[i]<tablrao[j]:
    #     tablrao.append(tablrao[i])
    #     i=i+1
    # else:
    #     tablrao.append(tablrao[j])
    #     j=j-1

    i=i+1
    j=j-1
print('le tableau inversé  est ',tablrao)