print("b")
print("r")
print("j")
print("u")
print("o")
print("n")
print("e")
gain=0

question=input("veuillez saisir les mots qu'on peut ecrire avec ces lettres")
question2=int(input("combien de mots avez vous trouvez "))
if question=="bonjour " and question=="jour " and question=="journer " and question=="our " and question=="bon " :
    gain=gain+1
elif question2==5:
    gain=gain+1
print("vous avez gagné ",gain ,"points") 