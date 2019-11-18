# 5 mots cles pour definir une function: 
#1. def: une fonction en python commence toujours par def 
#2. nom de la function 
#3. argument de la function: valeur d' entree de la function (c' est optionnel)
#4. le corps de la function: le code que execute la function
#5. la valeur retourner par la fonction

#exemple
def clean_text(string_value):
    cleaned_value = string_value.replace(",", " ")
    return(cleaned_value)

sentence = "Python,est,incroyable"
sentence = clean_text(sentence)
print(sentence)


#ecriture d' une function qui prend en parametre un texte et le renvoi sans ponctuation
jordan = open("texte.txt", "r", encoding="utf-8")
def clean_text2(parameter):
    nathan = parameter.replace(",", "")
    nathan = nathan.replace(".", "")
    nathan = nathan.replace("\n", "")
    nathan = nathan.lower() # mettre le texte sous minuscule
    return(nathan)

parameter = jordan.read()
jules = clean_text2(parameter)

print(jules)

# passer de majuscule a minuscule et vice-versa

words = "Zinedine ZIDANE France"
lower_words = words.lower()
print(lower_words)
