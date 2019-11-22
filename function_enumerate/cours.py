#utiliser  la function enumerate() pour afficher des elements de deux listes
# c' est en fait comment faire pour faire interagir deux listes differentes

cars = [["Noir", "Peugeot", "308"], ["Blanche","Audi", "A4"]]
price = [23000, 49000]

for i, car in enumerate(cars):
    car.append(price[i])
print(cars)
# et on affiche "cars". le prix sera entre dans la liste de liste cars
