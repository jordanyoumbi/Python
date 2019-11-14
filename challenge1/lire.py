f = open("unisex-names.csv", "r")

names = f.read()
names_list = names.split() # conversion de la variable "names" en une liste "names_list"
jordan = names_list[0:10] # afficher les 10 premier caractère la liste names_list
print(jordan)
