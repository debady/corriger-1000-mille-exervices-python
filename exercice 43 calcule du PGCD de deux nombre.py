a=int(input("veuillez saisir la valeurs de A :"))
b=int(input("veuillez saisir la valeurs de A :"))
c=0
PGCD=0
if a<b:
    mini=a
else:
    mini=b
for i in range(1,mini+1):
    if a%i==0 and b%i==0:
        PGCD=i
print("le PGCD de ",a,"et ", b, "est ",PGCD)
    
    
    
    
    
