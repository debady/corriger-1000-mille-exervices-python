# dabord il faut installer le module pip install pywhatkit
import pywhatkit as kit 

# ecrire un texte en manuscrire
kit.text_to_handwriting('hello word')

#faire une recherche avec un mot cle
kit.info('ivory cost')    

# afficher le resultats dde recherche dns le navigateur
kit.search("python")

# envoi de mssge
kit.sendwhatmsg('+2250544704854','bonjour david',22,30)

#recherche video youtube
kit.playonyt('tapis velo ')