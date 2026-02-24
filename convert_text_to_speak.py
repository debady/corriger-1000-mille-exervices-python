import pyttsx3
engine=pyttsx3.init()
engine.say("i will speak this text")
engine.runAndWait()


# pour mettre en francais
import pyttsx3
engine=pyttsx3.init()
voice=engine.getProperty("voices")[0]
engine.setProperty("voice", voice.id)

engine.say('avant de faire le programme il va falloir installer le module pip install pyttsx3.')
engine.runAndWait()