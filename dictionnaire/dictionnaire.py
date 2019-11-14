# un dictionnaire est comme une liste mais avec des cles qui pointe sur une valeur

# syntaxe d' un dictionnaire: dictionnaire = {} un peu commen liste: lister = []

scores = {} # dictionnaire vide

scores["Nina"] = 14

print(scores)

# ajout d' autre elements dans le dictionnaire "score"

scores["Thomas"] = 16
scores["Sarah"] = 17
scores["Matt"] = 15

print(scores)

# une autre maniere de declarer des listes

animals = {"poules": 120, "chevres": 46, "chevaux": 23, "vaches": 56}
print(animals) # on verra que le dictionnaire ne garde pas l' ordre de rentrees elements

# modification du dictionnaire animals

# modification de l'element poules
animals['poules'] = 110
animals['chevaux'] = animals['chevaux'] + 10
print(animals)

scores["Marie"] = 15
scores["Nina"] = scores["Nina"] + 2

scores["Thomas"] = scores["Thomas"] - 10

print(scores)

