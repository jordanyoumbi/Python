# exercice sur les comprehensions de listes
# pourcourir une liste et identifier ses colonnes

name_counts = {}

jules = open("legislators.csv", "r", encoding="utf-8")

legislators = jules.read()

for row in legislators:
    gender = row[3]
    year = row[7]
    if gender =="F" and year > 1950:
        name = row [1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
print (name_counts)