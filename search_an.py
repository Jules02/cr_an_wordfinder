# j'importe les modules nécessaires

from xml.dom import minidom

import time

start_time = time.time()


def getNodeText(node):
    # récupére le texte depuis le contenu d'une balise xml donnée
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)


# on va pouvoir récupérer les différents fichiers directement depuis internet ici
file = ("CRI_20111004_083.xml")

doc = minidom.parse(file)

x = 0

nb_para = doc.getElementsByTagName("Para")  # je récupère le nombre de balises à extraire

for n in range(nb_para.length):
    Para = doc.getElementsByTagName("Para")[n]  # récupère le contenu de la balise xml Para
    text = getNodeText(Para)
    lctext = text.lower()  # je mets tout en minuscule pour ne pas louper les occurences en majuscule
    wordlist = lctext.split()
    for w in wordlist:
        if w in {"distribution", "paradis"}:
            x += 1

print(x)


print("%seconds" % (time.time() - start_time))