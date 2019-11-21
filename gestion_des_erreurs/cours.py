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

