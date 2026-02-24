a=float(input("veuillez saisir la valeur de A : "))
b=float(input("veuillez saisir la valeur de B : "))
if a*b>0 and a*(-1)>0 and b*(-1)>0:
    print(a,"et ",b,"ont le meme signe et ! leurs signe est -")
elif a*b>0 and a*(-1)<0 and b*(-1)<0 :
    print(a,"et ",b,"ont le meme signe ! leurs signe est +")
    
    
elif a*b<0 and a*(-1)<0 and b*(-1)>0  :
    print(a,"et ",b, "sont deux signe differents ! et le signe de", a," est + et le signe de", b ,"est -")
elif a*b<0 and a*(-1)>0 and b*(-1)<0  :
    print(a,"et ",b, "sont deux signe differents ! et le signe de", a ,"est - et le signe de", b ,"est +")