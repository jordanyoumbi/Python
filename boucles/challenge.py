# creer un liste d' entier qui contient le nombre les numeros de tout les noms de la liste

rows_ancien = ["jordan,65", "yaounde,56", "biden,6563", "trump,565", "family,879", "russia,532", "pelosi,2345", "harris,7914", "kamala,1453", "testons,6669", "bill,65"]

int_dep_populations = []

for row in rows_ancien:
    jordan_row = row.split(",")
    nathan_row = int(jordan_row[1])
    int_dep_populations.append(nathan_row)
print(int_dep_populations)
