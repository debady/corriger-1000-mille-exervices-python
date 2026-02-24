i=0
pair=[]
impair=[]
liste=[32,5,12,8,3,75,2,15]
while i<len(liste):
    if liste[i]%2==0:
        pair.append(liste[i])
    else:
        impair.append(liste[i])
    i=i+1
print("les nombres pairs sonts ",pair)
print("les nombres impairs sonts ",impair)