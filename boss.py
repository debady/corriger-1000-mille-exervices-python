Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.chdir("c\\fichier")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.chdir("c\\fichier")
FileNotFoundError: [WinError 3] Le chemin d’accès spécifié est introuvable: 'c\\fichier'
>>> >>> import os
>>> os.chdir("c\\fichiers")
SyntaxError: invalid syntax
>>> impoert os
SyntaxError: invalid syntax
>>> import os
>>> os.chdir("c\\fichiers")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.chdir("c\\fichiers")
FileNotFoundError: [WinError 3] Le chemin d’accès spécifié est introuvable: 'c\\fichiers'
>>> import os
>>> os.chdir("c\\fichiers")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.chdir("c\\fichiers")
FileNotFoundError: [WinError 3] Le chemin d’accès spécifié est introuvable: 'c\\fichiers'
>>> import os
>>> print(os.getcwd())
>>> os.chdir("c:\\fichiers")
>>> print(os.getcwd())
