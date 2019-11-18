fichier = open("madrid-weather-2016.csv", "r")

jordan = fichier.read()

nathan = jordan.split("\n")

weather = []

#print(nathan)

for text in nathan:
    jules = text[1]
    nathan.append(jules)

print(nathan)
