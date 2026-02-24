print("veuillez saisir mots quelquonc ! ")
quest=input()
i=0
b=""
s=len(quest)-1
while i<len(quest):
    b=b+quest[s]
    i=i+1
    s=s-1
if b==quest:
    print(quest,"est un mots palindrome")
else:
    print(quest," n'est pas un mots palindrome")
