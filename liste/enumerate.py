#Nouvelles fonctions interessantes enumerate() et items()

# faire communiquer 2 listes. avec la fonction enumerate on pourra prendre chaque element d' une liste et le faire communiquer avec un element d' une autre liste

# on declare 2 listes
students =["Anna", "Martin", "Bob", "eric", "elise"]
ages = [16, 15, 18, 20, 20]

# Avec la fonction enumerate chaque students aura un age
# Mais cette fonction suivante est incomplete car elle ne prend pas en compte la valeur de l' age


for i, student in enumerate(students):
    print("Index Etudiant")
    print(i)
    print("Etudiant")
    print(student)


# cette fonction est complete car elle en compte chaque valeur de la liste ages

for i, student in enumerate(students):
    print("prenom")
    print(student)
    print("age")
    print(ages[i])

# Autre exemple sur l' ajout d' un element dans une liste de liste

cars = [["Noir", "Peugeaut", "308"], ["Blanche", "Audi", "A4"]]
price = [23000, 49000]

for i, car in enumerate(cars):
    car.append(price[i])
print(cars)