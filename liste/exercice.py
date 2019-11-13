# creation d' une liste vide nommer countries et temperatures
countries = []
temperatures = []
countries.append("France")
temperatures.append(122.5)
countries.append("spain")
countries.append("Canada")
temperatures.append(124.0)
temperatures.append(105.2)

france = countries[0]
france_temperature = temperatures[0]
print(france)
print(france_temperature)

# comment recuperer la longueur d' une liste: function len

int_months = [1,2,3,4,10,34,32,123,34,123,32]
total_length = len(int_months)
print(total_length)

# comment connaitre la valeur de la derniere variable dans une liste

last_value_position = len(int_months) - 1
last_value = int_months[last_value_position]
print(last_value)


# faire l' addition du nombre d' elements de chaque liste

countries = ["France", "spain", "United states", "Canada", "australisa"]
temperatures = [122.5, 124.0, 134.1]

sum = len(countries) + len(temperatures)
print(sum)


# recuperer plusieurs valeurs d' une meme liste

months = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "juin", "juillet", "Aout", "Septembre", "octobre", "Novembre", "Decembre"]
months_slicing_1 = months[4:6] # positions 4 et 5. 6 exclu: Mai et juin
print(months_slicing_1) # il afficgera ['Mai', 'juin']

   # afficher les valeur àartir de la position 5 (index 5 pas le nombre 5)
months_slicing_2 = months[5:]
print(months_slicing_2) # cela affichera ["juin", "juillet", ...."Decembre"]
