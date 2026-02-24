liste=[32,5,12,8,3,75,2,15]
gdrs=liste[0]
i=0
while i<len(liste):
    if gdrs<liste[i]:
        gdrs=liste[i]
    else:
        gdrs=gdrs
    i=i+1
print("le plus grands est ", gdrs)

# autre maniere de faire tout simple
liste=[32,5,12,8,3,75,2,15]
print("le plus grands elements de cette listes est",max(liste))
