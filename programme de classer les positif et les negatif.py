a=[14,-45,52,87,96,-4,-6,4,-5]
tab_posi=[]
tab_neg=[]
somme_posi=0
somme_nega=0
x=0

while x<len(a):
    if a[x]*(-1)>0:
        tab_posi.append(a[x])
        somme_posi=somme_posi+a[x]
    else:
        tab_neg.append(a[x])
        somme_nega=somme_nega+a[x]
        
    x=x+1
print("les nombre positifs sont : ",tab_posi)
print('leur somme est',somme_posi)
print()
print("les nombre negatifs sont : ",tab_neg)
print('leur somme est ',somme_nega)