question = int(input("combien de photocopie aimerai vous imprimer ? :"))
if question==10:
    s=question*50
elif question >=11 <=30:
    s=10*50+(question-10)*25
else:
    s=(10*50)+(20*25)+(question-30)*20
print("vous serai facturé alors a ", s, "FCFA")