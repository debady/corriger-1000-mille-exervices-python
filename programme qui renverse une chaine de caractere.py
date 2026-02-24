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
print(c)
if c==b:
    print("{} est un palindromme ".format(b))
else:
    print("{} n'est pas un palindromme ".format(b) )