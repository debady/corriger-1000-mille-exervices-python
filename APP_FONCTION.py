# def table7():
#     n=1
#     while n<11:
#         print(7,"*",n,"=",n*7)
#         n=n+1
# # fin des bloc de fonction
        
        
        
# table7()


# # ex2


# def table(base):
#     n=1
#     while n<11:
#         print(base,"*",n,"=",n*base)
#         n=n+1
# table(13)




# # table multiplpe


# def  tablemulti(base,debut,fin):
#     print('fragment de la table de multiplication par ',base ,':')
#     n=debut
#     while n<=fin:
#         print(n,'x',base,'=',n*base)
#         n=n+1
# tablemulti(58, 13, 17)




# # 



def inverse (ch):
    i=0
    b=""
    c=len(ch)-1
    while i<len(ch):
        b=b+ch[c]
        c=c-1
        i=i+1
    return b
print("veullez saisir un mots a inverser :")
b=input()
c=inverse(b)
if c==b:
    print("{} est un palindromme ".format(b))
else:
    print("{} n'est pas un palindromme ".format(b) )