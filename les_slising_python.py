Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=list(range(10,16))
>>> a
[10, 11, 12, 13, 14, 15]
>>> a[1:5]
[11, 12, 13, 14]
>>> a[0:3]
[10, 11, 12]
>>> a[0:6]
[10, 11, 12, 13, 14, 15]
>>> a[:]
[10, 11, 12, 13, 14, 15]
>>> l=[65,31,9,32,81,82,46,12]
>>> l[-5]
32
>>> a[2:-2]
[12, 13]
>>> s=a[1:6:2]
>>> s
[11, 13, 15]
>>> s=a[1:5:3]
>>> s
[11, 14]
>>> s=a[0:6:1]
>>> s
[10, 11, 12, 13, 14, 15]
>>> s=a[:2]
>>> s
[10, 11]
>>> l=list(range(10,20))
>>> l
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> t="ABCD"
>>> t
'ABCD'
>>> l[2:8]=t
>>> l
[10, 11, 'A', 'B', 'C', 'D', 18, 19]
>>> l[2:8]=5
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l[2:8]=5
TypeError: can only assign an iterable
>>> l[2:8]=[5]
>>> l
[10, 11, 5]
>>> l=list(range(10,20))
>>> l[2:8]=[5]
>>> l
[10, 11, 5, 18, 19]
>>> mots=['jambon','fromage','continue','chocolat']
>>> mots[2:2]=['miel']
>>> mots
['jambon', 'fromage', 'miel', 'continue', 'chocolat']
>>>  mots=['jambon','fromage','continue','chocolat']
 
SyntaxError: unexpected indent
>>> mots=['jambon','fromage','continue','chocolat']
>>> mots[2:5]=[]
>>> mots
['jambon', 'fromage']
>>> mots=['jambon','fromage','continue','chocolat']
>>> mots[1:]=['mayonnais','poulets','tomate'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> mots[1:]=['mayonnais','poulets','tomate']
>>> mots
['jambon', 'mayonnais', 'poulets', 'tomate']
>>> mots=['jambon','fromage','continue','chocolat']
>>> mots[2:5]=[]
>>> mots
['jambon', 'fromage']
>>> #vouloir
>>> 