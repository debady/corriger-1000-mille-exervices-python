# gerer les error de division impossible

while True:
    try:
        x=int(input("entrez un numerateur : "))
        y=int(input("entrez le denominateur : "))
        print("le resultats de la disision est : ",x/y)
    except :
        print("erreur :impossible de d'effectuer la division !")
        print("veuillez reesaiyé")
    finally:
        print("le programme est terminer " )
    break

        
# afficher un message precise4



while True:
    try:
        x=int(input("entrez un numerateur : "))
        y=int(input("entrez le denominateur : "))
        z=x/y
    except ValueError:
        print(ValueError)
        print("erreur :la valeurs enter n'est pas correct ou  n'est pas un entier !")
    except ZeroDivisionError:
        print("erreur :impossible de d'effectuer la division !")
    else:
        print("le resultats de la disision est : ",z)
        
    finally:
        print("le programme est terminer " )
    continue
