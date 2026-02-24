print("veuillez saisir le mot :")
a=input()
b=""
rep=len(a)-1
i=0
while i<len(a):
    b=b+a[rep]
    rep=rep-1
    i=i+1
if (a==b):
    print("le mot est un palindrome")   
else:
    print("le mot n est pas un palindrome")
print(b)
    

