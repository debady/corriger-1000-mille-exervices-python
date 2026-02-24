import math

valA =int(input('la valeurs de A :'))
valB =int(input('la valeurs de B :'))
valC =int(input('la valeurs de C :'))

delta = valB**2-4*valA*valC

if delta <0:
    print('pas de solution')
elif delta==0:
    solu= (-valB)/(2*valA)
    print("la solution est ",solu)
else:
    solu1 = (-valB-math.sqrt(delta))/(2*valA)
    solu2 = (-valB-math.sqrt(delta))/(2*valA)

    print("les  solutions sont ",format(solu1,".2f")," et",format(solu2,".2f"))