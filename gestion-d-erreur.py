while True:
    try:
        var1 = int( input('veuillez saisir le 1er nombre:... '))
        var2 = int( input('veuillez saisir le 2ème nombre:... '))
        varResultats = var1/ var2

        print('la division de ',var1,' par ',var2,' = ',varResultats)
    except ValueError:
        print('Incorrect Réesayer !! :')
        continue
    except ZeroDivisionError:
        print('la division de ',var1,' par ',var2,' n\'est pas possible\n')
        print(f'la division de {var1} par {var2} n\'est pas possible')
        continue