# rendre le fichier us birth en liste, puis en une liste de liste

jules = open("US-births-2000-2014.csv", "r", encoding="utf-8")

jordan = jules.read()

liste2 = jordan.split("\n")
liste = liste2[1:]
#for nathan in liste:
#print(liste[0:10])
def read_csv(liste):
#    nouveau = liste.split(",")
    final_list = []
    for new in liste:
        int_fields = []
        nouveau = new.split(",")
        for new in nouveau:
            int_fields.append(int(new))
        final_list.append(int_fields)
    return(final_list)

maman = read_csv(liste)
print(maman[0:10])

# function qui calcul le nombre de naissance par mois

def month_birth(liste):
    birth_per_month = {}

    for li in liste:
        month = li[1]
        births = li[4]

        if month in birth_per_month:
            birth_per_month[month] += births
        else:
            birth_per_month[month] = births
    return(birth_per_month)

us_month_births = month_birth(maman)
print(us_month_births)


# function qui affiche le nombre de naissance de la semaine

def day_birth(liste):
    birth_per_day = {}
    for li in liste:
        day = li[3]
        births = li[4]
        if day in birth_per_day:
            birth_per_day[day] += births
        else:
            birth_per_day[day] = births
    return(birth_per_day)

us_days_births = day_birth(maman)
print(us_days_births)

# creer une function plus generale
