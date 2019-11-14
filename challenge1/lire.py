f = open("unisex-names.csv", "r")

n = 0
Baby = "Baby"
names = f.read()
names_list = names.split() # conversion de la variable "names" en une liste "names_list"
jordan = names_list[0:10] # afficher les 10 premier caractère la liste names_list
print(jordan)

# crrer une liste dans une autre liste

jordan2 = []
for nathan in jordan:
    text = nathan.split(",") #convertir chaque elements en une liste particuliere
        #   jules = int(text[1])
    jordan2.append(text)
print(jordan2)


# conversion en nombres decimaux
numerical_list = []
for x in names_list:
    young = x[1]
    data = float(young)
    numerical_list.append(data)
print(numerical_list)

# retrouver un meme prenom avec 1000 occurences dans la liste

final_list = []
for nanou in numerical_list:
    name = line[0]
    population = line[1]
    if population >= 1000:
       final_list.append(name)
print (final_list)
