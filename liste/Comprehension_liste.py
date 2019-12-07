# reduction du calcul à partir de fonction dejà defini
# exemple ci-dessous comment calculer la longueur des elements d' une liste

animals = ["Chien", "Tigre", "Lion", "vache", "Panda"]

animals_lengths = []
for animal in animals:
    animals_lengths.append(len(animal))
print(animals_lengths)

# le code ci-dessous fait 4 lignes alors que nous aurons pu le faire plus simplement avec des functions dejà) faite

animals_lengths_2 = [len(animal) for animal in animals]
print(animals_lengths_2)

# les comprehensions de liste sont donc plus compacts

# autres exemple. doublons toute les valeurs d' une liste
prices = [10, 45, 156, 7800]
prices_doubled = [price * 2 for price in prices]
print(prices_doubled)

