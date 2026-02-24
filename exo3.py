
print('\nveuillez saisir le nom du client :')
varNomClient = input('...:')
print('veuillez saisir le numero de la facture :')
varNumFact = input('...:')

print('veuillez saisir la date de la facture :')
varDateFacture = input('...:')

#  sesssion de produit
print('veuillez saisir le numéro du produit :')
varNumProd = input('...:')

print('veuillez saisir le libelle du produit  :')
varLibProd= input('...:')

print('veuillez saisir la quantité :')
varQuteProd = int(input('...:'))

print('veuillez saisir le prix unitaire :')
varPuProd  = int(input('...:'))

tht=0
rem =0
mp = varPuProd * varQuteProd
tht = tht+mp
varetat ="Achat de Moins de 50.000 XOF donc pas de réduction"

if tht>50000 and tht<= 100000:
    rem = tht*0.05
    varetat = "Valeur d'achat compris entre 50.000 XOF et 100.000 XOF donc une  Réduction de 5%"
elif tht>100000:
    rem=tht*0.1
    varetat = "Valeur d'achat est plus de 100.000 XOF donc  Réduction une de 10%"


np = tht-rem
print("\nla facture N° :",varNumFact,'\ndu le client ',varNomClient,"\nInitié le :",varDateFacture,"\n")
print("la somme total est :",tht," XOF\n",varetat)
print("le montant net àpayer  est :",np,"XOF\n")

print("voulez vous saisir entrer un autre produit O pour (OUI) N pour (NON) ")
resp = input('...:')

while resp != 'N' or resp != 'O' or resp != "n" or resp != 'o':
    print('Incorret ! veuillez saisir soit N pour (NON) et O pour (OUI)')
    resp=input('...:')

    if resp =="N" or resp =="n":
        break
    else:
        continue
