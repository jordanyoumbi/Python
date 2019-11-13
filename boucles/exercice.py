final_data = []

rows_ancien = ["jordan,65", "yaounde,56", "biden,6563", "trump,565", "family,879", "russia,532", "pelosi,2345", "harris,7914", "kamala,1453", "testons,6669", "bill,65"]

for i in rows_ancien:
    jordan = i.split(",")
    final_data.append(jordan)
#print(final_data)
print(final_data[0:5])

first_list = final_data[0]
print(first_list)

first_list_first_value = final_data[0][0] #1ere liste 1er element
print(first_list_first_value)

second_list_first_value = final_data[1][0] # 2eme liste 1er element
print(second_list_first_value)

second_list_first_value = final_data[1][1] # 2eme liste 2er element
print(second_list_first_value)


# Boucle àtravers une liste de listes

five_elements = final_data[0:5]

departements_list = []

departements_list.append(five_elements[0][0])
departements_list.append(five_elements[1][0])
departements_list.append(five_elements[2][0])
departements_list.append(five_elements[3][0])
departements_list.append(five_elements[4][0])

print(departements_list)

departement_populations = []

for row in five_elements:
     departement_population = row[1]
     departement_populations.append(departement_population)

print(departement_populations)

# crer une liste departements_list qui contient tous les noms des departements de final_data

five_elements_nom = final_data[0:5]

departements_nom = []

departements_nom.append(five_elements_nom[0][0])
departements_nom.append(five_elements_nom[1][0])
departements_nom.append(five_elements_nom[2][0])
departements_nom.append(five_elements_nom[3][0])
departements_nom.append(five_elements_nom[4][0])

print(departements_nom)

departement_populations_nom = []

for row in five_elements_nom:
    departement_population_nom = row[0]
    departement_populations_nom.append(departement_population_nom)

print(departement_populations_nom)

