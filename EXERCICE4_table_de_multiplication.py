# bloc des fonction

def table7():
    n=1
    while n<11:
        print(7,"*",n,"=",n*7)
        n=n+1
# fin des bloc de fonction
        
        
        
table7()


# ex2


def table(base):
    n=1
    while n<11:
        print(base,"*",n,"=",n*base)
        n=n+1
table(13)




# table multiplpe


def  tablemulti(base,debut,fin):
    print('fragment de la table de multiplication par ',base ,':')
    n=debut
    while n<=fin:
        print(n,'x',base,'=',n*base)
        n=n+1
tablemulti(58, 13, 17)



# 