phrase  = input('veuillez saisir une phrase :')

nbreEspace = 0 
tab = []
mot = ''
espace = ' '
for i in range(len(phrase)):
	if phrase[i]!=' ':
		mot=mot+phrase[i]
		tab.append(mot)
	tab.append(espace)

# 	tab.append(phrase[i])
# 	if phrase[i] == " ":
# 		nbreEspace = nbreEspace+1
		
# print(nbreEspace)
# print(len(phrase))
print(mot)
