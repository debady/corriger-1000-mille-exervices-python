import random
numero_tel = []
tab_div_numer = []

numero_tel_moov  = []
numero_tel_orange  = []
numero_tel_mtn  = []

x = 0
while x < 300:
    
    generer_numero_tel= random.randint(2345678, 99999999)
    generer_numero_tel=str(generer_numero_tel)
    numero_tel.append(generer_numero_tel)
         
    x = x+1
#    

r=[]
for i in range(0,100):
    r.append(numero_tel[i] + "\n")




s=[]
for n in range(100,200):
    s.append(numero_tel[n] + "\n")
    
    
t=[]
for l in range(200,300):
    t.append(numero_tel[l] + "\n")
    
print("les ",len(r)," premiere numeros sont" + "\n")
print(" ".join(r))
print()

print("les ",len(s)," suite numeros sont" + "\n")
print(" ".join(s))
print()

print("les ",len(t)," dernier numeros sont" + "\n")
print(" ".join(t))

somme=len(r)+len(t)+len(s)

print("le tout fait",somme)