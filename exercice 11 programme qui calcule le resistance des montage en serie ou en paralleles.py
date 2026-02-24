r1=int(input("veuillez saisir la resistances R1 : "))
r2=int(input("veuillez saisir la resistances R2 : "))
r3=int(input("veuillez saisir la resistances R3 : "))
res_serie=r1+r2+r3
res_par=(r1*r2*r3)/(r1*r2+r1*r3+r2*r3)
print("la resistance en serie est ", res_serie)
print("la resistance en paralle est ", res_par)