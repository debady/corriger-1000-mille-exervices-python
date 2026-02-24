import random as rd 

t1 = []
t2 = []
t3= []

for i in range(5):
    entier = rd.randint(-99999,99999)
    t1.append(entier)


    entier = rd.randint(-99999,99999)
    t2.append(entier)

n=len(t1)
m=len(t2)
k=0
i=0
j=0

while  i<n and j<m:
    if t1[i]<t2[j]:
        t3.append(t1[i])
        i=i+1
    else:
        t3.append(t2[j])
        j=j+1

print()
print(t1)
print()
print(t2)
print()
print(t3)
