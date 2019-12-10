# les dataScientist ont souvent besoin d'organiser les chaines de caractère pour extraire des inforamtions importante
# comment rechercher le debut d' une chaine de caractère
# ^ represente la recherche du debut d' une chaine de carcetère
# $ represente la recherche de la fin d' une chaine de carcatère

strings =["il est  sur le feu", "fou"]
bad_string = "un feu de paille"
regex = "f.u$"
# ce regex marchera uniquement pour strings car u represente bien la fin d' une chaine de cararctère. mais ce n' est pas le cas pour bad_string
import csv

f = open("askreddit-2015.csv", encoding='utf-8')
csvreader = csv.reader(f)
posts = list(csvreader)
print(posts[0:5])

for post in posts[:10]:
    print(post)

# Maintenant nous allons utiliser les regex dans les fonctions
# utilisation du module re
import re

if re.search("f.", "kung fu") is not None:
    print("trouvé")
else:
    print("aucune correspondance")

# Training

import re

of_reddit_count = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count += 1
print(of_reddit_count)

# Crochets pour matcher plusieurs lettres
# utiliser les crochets pour matcher les recherches multiple

of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None: # ici on va aussi prendre en compte les reddit qui commence par r miniscule
        of_reddit_count += 1
print(of_reddit_count)

# Comment ignorer les caractè!re speciaux
# pour ignorer les chaines de carctères on utilise "\"

serious_count = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count += 1
print(serious_count) # ceci affichera tout le nombre total de [Serious] dans le fichier
# cela permet à pyhton de comprendre de ne pas confondre avec une regex comme [Rr]eddit. donc on met donc \ quand on bveux ignorer des caractère

# Training
# Compter le nombre de poste qui  contiennent des tags (serious)-(Serious)-[Serious]-[serious]
serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1
print (serious_count)

# Comment combiner plusieurs regex

#Training
# determiner le nombre d' occurence ou on commence par [\[\(][Ss]erious[\]\)] et qui termine par [\[\(][Ss]erious[\]\)] et fait ensuite l' ensemble
serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_start_count += 1
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_end_count += 1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_count_final += 1
print(serious_start_count)
print(serious_end_count)
print(serious_count_final)
# nous pouvons donc combiner plusieurs regex avec pipe (|)

# Comment modifier les chaines de carctères avec les regex
# pour ce faire nous utiliserons la fonction sub() du module re
# sub() prend 3 caractères en entrée, le premier element c' est l'element recherché, le 2eme c' est celui qui remplacera, le 3eme c' est la chaine de caractère qui possede le premier element
# si il y a aucun match entre le premier element et le 3eme element alors on garde la chaine d' origine
import re

posts_new = []
for row in posts:
    row[0] = re.sub("[\[\(][Ss]erious]\)\]", "[Serious]", row[0])
    posts_new.append(row)
print(posts_new[0:10])

# Comment matcher les années avec regex
# voici comment on defini de 1000 à 2999. [1-2][0-9][0-9][0-9] ou pour eviter la repetition de [0-9], on peux utiliser des accolades. ex: [1-2][0-9]{3}, on dit donc qu' il y aura [0-9] 3 fois

year_string = []
for string in strings:
    if re.search("[1-2][0-9]{3}", string) is not None:
        year_string.append(string)
print(year_string)

# extraire des années
#pour cela on utilisaera la fonction findall importé du module re
# la fonction findall nous renvoi une liste en sortie
jordan = re.findall("[a-z]", "abc12344")
print(jordan)
# un exemple supplementaire
string_years = "On est deja en 2017, une année de plus que 2016 et une de moin que 2018"
years = re.findall("[1-2][0-9]{3}", string_years)
print(years)

# Utilisation du module datetime pour tranformer le format des dates
import datetime
import time
#for row in posts:
#    float_stamp = float(row[2])
#    day = datetime.datetime.fromtimestamp(float_stamp)
#    row[2] = day
#print(posts[0:5])
#may_count = 0
#for row in posts:
#    if row[2].month == 5:
#        may_count += 1
#print(may_count)

