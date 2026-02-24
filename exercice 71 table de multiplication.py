def table_de_multiplication(quest):
    for i in range(1,11):
        
        print(i,"*",quest,"=",i*quest)
while True:
    quest=int(input("veuillez saisir votre table souhaiter :"))
    if quest>0:
        break
table_de_multiplication(quest)
