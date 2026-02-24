from bs4 import BeautifulSoup
import webbrowser

html = BeautifulSoup(
    '<h1>EPREUVE N°1</h1>'

    '<form action="#" method="get">'
        '<label for="#">NOUVEAU NOMBRE : <input type="number" name="nbre" value="10"></label>'
        '<input type="submit"  name="envoyer" value="valider"><a ><a href="index.php"></a>'
    '</form>', 'html.parser')

urle = "C:/NGUESSAN/indexAffiche.html"

with open('indexAffiche.html', 'w') as file:
    file.write(html.prettify())

webbrowser.get()
webbrowser.open(urle)