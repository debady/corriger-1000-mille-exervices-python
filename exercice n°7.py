i=0
tab=[]
n=input()
s=len(n)-1
b=""
tab.append(n)
while i<len(n):
    b=b+n[s]
    i=i+1
    s=s-1
print(b)
