weather_data = []

f = open("madrid-weather-2016.csv", "r")
data = f.read()

jordan = data.split("\n")
for nathan in jordan:
    test = nathan.split(',')
    weather_data.append(test)
print(weather_data[0:5])

# verification du nombre de jour d' une annee dans me fichier madrid-weather-2016 inclus l' entete du fichier qui n' est pas un jour

count = 0
for i in weather_data:
    count = count + 1
print(count)

# supprimer l' entete pour avoir le nombre de jour exacte

new_weather = weather_data[1:366]
print(new_weather)

# chercher de maniere rapide un caractere dans une liste

if "Soleil" in data:
    print("il avait du soleil")

# autre maniere rapide de verifier la presence d' un caractere dans une liste avec de boolean
# attention, cette methode est sensible a la casse
climat_found = "Soleil" in data
month_found = "janvier" in data
print(climat_found)
print(month_found)

# chercher les elements d' une plus petite liste dans une grande liste

weather_types = ["Pluie", "Soleil", "Nuage", "Nuage-Pluie", "Orage", "julelimat"]
weather_type_found = []
for i in weather_types:
    if i in data:
        print(i)
        weather_type_found.append(i)

print(weather_type_found)
