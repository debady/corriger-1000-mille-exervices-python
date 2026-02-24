while True:
    try:
        print("veuillez saisir un mumerateur ")
        a=int(input())
        print("veuillez saisir un denominateur ")
        b=int(input())
        x=a/b
        print( x)
    except ZeroDivisionError():
        print("la valeurs saisir est incorrect")
        pass