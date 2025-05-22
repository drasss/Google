
import urllib.request, urllib.error, urllib.parse

link="https://dossierscol.univ-pau.fr/mdw-vaadin-1.2.1/#!notesView"
url = link

reponse = urllib.request.urlopen(url)
contenu_web = reponse.read().decode('UTF-8')

f = open('obo-t17800628-33.html', 'w')
f.write(contenu_web)
f.close