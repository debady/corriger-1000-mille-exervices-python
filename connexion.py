MDP  = 'guessan'
SPEUDO = 'debady'
nbreEssai = 3


essaieSpeudo= input("veuillez saisir votre Speudo " )
essaieMDP = input("veuillez saisir votre MDP  " )


if essaieSpeudo == SPEUDO and essaieSpeudo == MDP:
    print(SPEUDO,'',MDP)
else:
    print(nbreEssai)
    nbreEssai = nbreEssai - 1

    while essaieSpeudo !=SPEUDO and essaieSpeudo !=MDP and nbreEssai<=0:
        print('plus le droit')
        print(nbreEssai)
        # essaieSpeudo= input("veuillez saisir votre Speudo " )
        # essaieMDP = input("veuillez saisir votre MDP  " )

        
        # if nbreEssai ==0 :
        #     print('vous n\'avez plus le droit')
        #     break
        # else:

        # if essaieSpeudo == SPEUDO and essaieSpeudo == MDP :
        #     print(SPEUDO,'',MDP)

        # elif nbreEssai==0:
        #     print('vous n\'avez plus le droit')
        #     break
        
        nbreEssai= nbreEssai -1


