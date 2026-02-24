# Un exemple de programme Python qui parle!
import time
import win32com.client
import pythoncom
# import thread

# Une fonction d'attente
def Attente(ObjetVoix):
	while ObjetVoix.Speakinggt:
		pythoncom.PumpWaitingMessages()
		# voix=win32com.client.Dispatch({EEE78591-FE22-11D0-8BEF-0060081841DE})
		# voix.Speak()

# # A adapter pour avoir la voix anglaise (suivant voix disponibles)
# voix.CurrentMode=7

# Texte = print ('ENGLISH SPEAKER')

# # inst = "Please type a text to read". To quit theprogram type 'end'.
# # print "instvoix.Speak(inst)"
# Attente(voix)

# while Texte != end:Texte = raw_input(gtgt )
#     voix.Speak(Texte)
#     Attente(voix)

# voix.Speak(Good bye.)
# Attente(voix)
# <br />Si on veux ajouter de la voix dans une application graphique (style TK ou WxWindows), il n'est pas neacutecessaire d'utiliser la fonction Attente
