# une liste a toujours des crochets [], il est toujours mieux de creer une liste vide en premier temps. months []
# si je veux ajouter une valeur dans une liste je le fait avec append()

months = []
# append()
months.append("janvier")
months.append("Fevrier")

print(months)
print(type(months))

days = []
days.append(1)
days.append("lundi")
days.append(2)
days.append("mardi")
print(days)

# autre maniere de declarer une liste

temperatures = ["france", 122.5, "spain", 124.0]
temperatures.append("united states")
temperatures.append(134.1)
print(temperatures)
