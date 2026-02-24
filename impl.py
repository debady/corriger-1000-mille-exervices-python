nbreEmployer  = int(input('\n veuillez saisir le nombre d\'employer :'))
plusPtt = 1
tab=[]
salmini = 9999999999

for i in range(1,nbreEmployer+1):
	print("veuillez saisir le salaire du ",i," ème employer ")
	salb = int(input())

	if salb>1 and salb<=90000:
		salNet = salb-(salb*0.02)

	elif salb>90000 and salb<=500000:
		salNet = salb-(salb*0.1)

	elif salb>500000:
		salNet = salb-(salb*0.25)
	
	# Mettre les valeurs des salaires net dans la table
	print("les salaires net des salaires saisir sont :",tab)
	tab.append(salNet)
	

	# if salNet<salmini:
	# 	salmini==salNet
	# 	print("le salaire minimun est ",salmini)

x= 0
plus_ppt = 1
while x<len(tab):
	if x ==0:
		plus_ppt=tab[x]
		print("\n la premier salaire net calculer est :",tab[x])

	# if plus_ppt ==tab[x]:
	# 	plus_ppt==plus_ppt

	if plus_ppt<=tab[x]:
		plus_ppt==tab[x]
		
	print(x+1," element du tableau est :",tab[x])
	x=x+1
print("\n les element du tableau sont :",tab)
print("le salaire le plus bas est :",plus_ppt )
	

	
	
	

	
	
	# # condition pour voir le salalire net plus bas
	# if plusPtt==1:
	# 	plusPtt = salNet # prémière iteration la condition est vrai du coup la variable qui doit contenir le salaire le plus bas prend la premier salaire net obtenu
	# 	print(plusPtt)
		
	# elif plusPtt==salNet: # si le plus petit salaire actuelle est égal au salaire qui vient d'être saisir alors il garde sa valeur
	# 	plusPtt ==plusPtt

	# elif plusPtt<=salNet: # le le nouveau salaire net calculer est plus petit que la valeur qu'il contenait alors efface son encienne valeur et prend celle ci
	# 	plusPtt ==salNet
	# print('le salaire net le plus bas actuellement est ',plusPtt)
	


# x= 0
# # plus_ppt = 1
# while x<len(tab):
# 	if x ==0:
# 		plus_ppt=tab[x]
# 		print("\n la premier salaire net calculer est :",tab[x])

# 	if plus_ppt ==tab[x]:
# 		plus_ppt==plus_ppt

# 	if plus_ppt<=tab[x]:
# 		plus_ppt==tab[x]
		
# 	print(x+1," element du tableau est :",tab[x])
# 	x=x+1
# print("\n les element du tableau sont :",tab)
# print("le salaire le plus bas est :",plus_ppt )