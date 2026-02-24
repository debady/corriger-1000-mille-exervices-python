a=int(input("veuillez saisir un nombre :"))
while a>0:
    b=a+1
    def table_multi(b):
        for i in range(1,11):
            print(i,"*",b,"=",i*b)
    a=a-1
    table_multi(b)