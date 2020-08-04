# j'importe les modules nécessaires

from xml.dom import minidom

import re
import time

start_time = time.time()


input_word = input("Terme à rechercher: ")


def getNodeText(node):
    # récupére le texte depuis le contenu d'une balise xml donnée
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)


count = 0

# on va pouvoir récupérer les différents fichiers directement depuis internet ici
file = "CRI_20111004_083.xml"

doc = minidom.parse(file)

nb_para = doc.getElementsByTagName("Para")       # je récupère le nombre de balises à extraire

for n in range(nb_para.length):
    para = doc.getElementsByTagName("Para")[n]   # récupère le contenu de la balise xml Para

    text = getNodeText(para)                     # contenu de la balise en string
    lctext = text.lower()   # je mets tout en minuscule pour ne pas louper les occurences en majuscule

    count += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(input_word), lctext))  # compte les occurences
    # plus économique que de passer par une liste avec split et permet de rechercher avec des inputs de plusieurs mots

print("\nLe terme '{s}' a été trouvé {d} fois dans les comptes rendus des séances de l'AN".format(s=input_word, d=count))


print("%s seconds" % (time.time() - start_time))