# coding: utf-8

# j'importe les modules nécessaires

from xml.dom import minidom

import re
import time
import os
import argparse

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


parser = argparse.ArgumentParser()
parser.add_argument("word", type=str, nargs="*", help="word(s) to be searched")
args = parser.parse_args()

input_word_list = []

if args.word:
    input_word_list = args.word
else:
    input_word_list.append(input("Terme à rechercher: "))

    while True:
        other_word = input("Rajouter un autre terme [n]: ")
        if other_word not in ['n', '']:
            input_word_list.append(other_word)
            pass
        else:
            break

print("\nSearching for {}...\n".format(input_word_list))

count = 0

directory = "2013"


i = 0
for fname in os.listdir(directory):
    i += 1
    print("Processing {file} ... ({current}/{range})".format(file=fname, current=i, range=len(os.listdir(directory))))
    if fname.endswith(".xml"):
        try:
            doc = minidom.parse(directory + "/" + fname)

            nb_para = doc.getElementsByTagName("Para")  # je récupère le nombre de balises à extraire

            for n in range(nb_para.length):
                para = doc.getElementsByTagName("Para")[n]  # récupère le contenu de la balise xml Para

                text = getNodeText(para)  # contenu de la balise en string
                lctext = text.lower()  # je mets tout en minuscule pour ne pas louper les occurences en majuscule
                unifiedtext = del_accent(lctext)

                for word in input_word_list:
                    count += sum(
                        1 for _ in
                        re.finditer(r'\b%s\b' % re.escape(del_accent(word)), unifiedtext))  # compte les occurences
                    # plus économique que de passer par une liste avec split et permet de rechercher avec des inputs de
                    # plusieurs mot
        except:
            print("Error processing {}".format(fname))
        continue
    else:
        continue


if len(input_word_list) == 1:
    print("\nLe terme '{s}' a été trouvé {d} fois dans les comptes rendus des séances de l'AN".format(s=input_word_list, d=count))
else:
    print("\nLes termes '{s}' ont été trouvés {d} fois dans les comptes rendus des séances de l'AN".format(s=input_word_list, d=count))


print("%s seconds" % (time.time() - start_time))
