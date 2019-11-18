# Ranger les planetes en function de leur longueur d' ecriture dans differentes listes

planet_names = ["Mercure","Venus","Terre","Mars","Jupiter","Sturne","Neptune","Uranus"]

long_names = []
short_names = []

for jordan in planet_names:
    if len(jordan) > 5:
        long_names.append(jordan)
    else:
        short_names.append(jordan)

print(long_names)
print(short_names)
