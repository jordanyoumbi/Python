# faire une liste de liste [[]]

cities_number = ["Paris,45", "Madrid,171", "Rome,12"]

final_list = []

for row in cities_number:
    split_list = row.split(',') # la fonction row.split() separe la liste les caracteres en fonction du caractere entre parentheses)
    final_list.append(split_list)
print(final_list)
