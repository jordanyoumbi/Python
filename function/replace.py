# remplacer les caractere par d' autres cararcteres dans un texte
# en occurence remplacer les pontuation et les lignes vides du fichier texte.txt

jordan = open("texte.txt", "r", encoding="utf-8")
nathan = jordan.read()
#print(nathan)

jules = nathan.replace(",", " ")
#print(jules)

lebron = jules.replace(".", "")

steph = lebron.replace("\n", " ")
print(steph)
