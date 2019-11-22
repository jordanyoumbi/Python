# use set() to remove duplicate

animals = ["Chien", "Tigre", "Chat", "Chat", "Chien", "Chien"]
unique_animals = set(animals)
print(unique_animals)

# add()

unique_animals.add("Tortue")
print(unique_animals)

# remove()
unique_animals.remove("Chat")
print(unique_animals)

# list()
unique_animals = list(unique_animals)
print(unique_animals)

# utiliser try and execption
  # on fait un teste d' execption puisqu' on sait que l' espace ne peux devenir un entier
try:
    int('')
except Exception:
    print("impossible de convertir")

# maintenant on donne un nom l'exception

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

# exemple avec une liste

numbers = [1,2,3,4,5,6]
jordan = [56,65,32,23,5356,563536]
for i in numbers:
    try:
        int('')
    except Exception:
        print ("il ya une erreur")  # avec ca il affichera tout le temps "il y a une erreur" mais si n ne plus voir ca et continuer de faire tourner le code on peux faire "pass" àa place de print

# comme la
for i in jordan:
        try:
            int('')
        except Exception:
            pass



