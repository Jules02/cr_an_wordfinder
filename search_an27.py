# coding: utf-8

# j'importe les modules nécessaires

from xml.dom import minidom

import re
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


def del_accent(text):
    """ supprime les accents du texte """
    accents = {'a': ['à', 'ã', 'á', 'â'],
               'e': ['é', 'è', 'ê', 'ë'],
               'i': ['î', 'ï'],
               'u': ['ù', 'ü', 'û'],
               'o': ['ô', 'ö']}
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            text = text.replace(accented_char, char)
    return text


input_word = raw_input("Terme à rechercher: ")
unified_input_word = del_accent(input_word)


count = 0

# on va pouvoir récupérer les différents fichiers directement depuis internet ici
file = "CRI_20111004_083.xml"

doc = minidom.parse(file)

nb_para = doc.getElementsByTagName("Para")       # je récupère le nombre de balises à extraire

for n in range(nb_para.length):
    para = doc.getElementsByTagName("Para")[n]   # récupère le contenu de la balise xml Para

    text = getNodeText(para)  # contenu de la balise en string
    lctext = text.lower()  # je mets tout en minuscule pour ne pas louper les occurences en majuscule
    unifiedtext = del_accent(lctext)

    count += sum(
        1 for _ in re.finditer(r'\b%s\b' % re.escape(unified_input_word), unifiedtext))  # compte les occurences
    # plus économique que de passer par une liste avec split et permet de rechercher avec des inputs de plusieurs mots

print("\nLe terme '{s}' a été trouvé {d} fois dans les comptes rendus des séances de l'AN".format(s=input_word, d=count))


print("%s seconds" % (time.time() - start_time))