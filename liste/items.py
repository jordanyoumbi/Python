# methode Items permet d' acceder au clé et valeur d' un dictionnaire plus facilement

#cet Exemple va nous permettre d' afficher la clé et la valeur des elements dans un dictionnaire
# Pour cela ontilisaera une boucle pour

fruits = {
    "banane":9,
    "orange":15,
    "kiwi":4
}

# nous venon de definir le dictionnaire et maintenant nous allons exploiter les clés (fruit) et valeur (number) des elements de ce dictionaire à l' aide de items()

for fruit, number in fruits.items():
    print(fruit)
    print(number)