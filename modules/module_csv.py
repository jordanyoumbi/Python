# utiliser un module csv qui importe directement un fichier et le transforme en liste

import csv

f = open("nfl.csv")
csvreader = csv.reader(f)
nfl = list(csvreader)#  c'est la function list venu de import csv qui transformera directement mon fichier en liste

#print(nfl)

#compter le nombre de fois qu'une equipe a gagner le fichier csv

sf_wins = 0 
for row in nfl:
    if row[2] == "San Francisc 49ers":
        sf_wins += 1
print(sf_wins)


# Training: afficher le nombre de victoire de l' equipe giants

def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count += 1
    return(count)

my_giant_wins = nfl_wins("New York Giants")
print(my_giant_wins)

# Compter les victoires pour une annee donnee

def nfl_w(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count += 1
    return(count)

sf_2012_wins = nfl_w("San Francisco 49ers", "2012")
print(sf_2012_wins)


# programme qui prend en compte la classe et les objects(function)

class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv")
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)
    
    def count_total_wins(self):
        count = 0
        for i in self.nfl:
            if row[2] == self.name:
                count += 1
        return(count)

    def count_wins_in_year(self, year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == year:
                count += 1
        return(count)

niners = Team("san franscisco 49ers")
niners_wins_2013 = niners.count_wins_in_years("2013")
print(niners_wins_2013)
