# Tockenization du vocabulaire(conversion du vocabulaire en une liste). et apres on converti le texte en petit composant d' une liste

vocabulaire = open("dictionnaire.txt", "r", encoding="utf-8").read()
#print(vocabulaire)

tokernization_vocabulary = vocabulaire.split(" ")
print(tokernization_vocabulary[0:5])
