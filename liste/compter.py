# Compter les elements d' une liste et presenter les resultats dans un dictionnaire

# si un element faisant partir d' une liste est dans le dictionnaire alors on ajoute 1 a cette element mais si l' element n' y est pas dans le dictionnaire alors on cree l' element dans le dictionnaire

fruits = ["citron","Banane","pomme","pomme","pomme","Banane","Banane","pomme"]

fruit_count = {}

for jordan in fruits:
    if jordan in fruit_count:
        fruit_count[jordan] = fruit_count[jordan] + 1
    else:
        fruit_count[jordan] = 1

print(fruit_count)
