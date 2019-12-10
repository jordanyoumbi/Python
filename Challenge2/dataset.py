# Utilisation des comprehensions de liste et des liste de liste avec un dataset
# dans le code suivant nous dechiffrons une date set pour ressortir toute les années ou les joueurs ont eu des penalité

import csv

f = open("nfl-suspensions-data.csv")
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:]
#print(nfl_suspensions)

years_colomn = nfl_suspensions[5]
years = {}

for suspension in nfl_suspensions:
    row_year = suspension[5]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1

print(years)

# Par la suite recuperer les valeurs unique de la colonne team (deuxieme valeur de liste) en utilisant les comprehension de liste et transformer ces element en disctionnuaire
teams = [row[1] for row in nfl_suspensions]
unique_teams = set(teams)
print(unique_teams)
# noius faisons pareil pour le 3 elements de colonne qui est  "game"
games = [row[2] for row in nfl_suspensions]
unique_games = set(games)
print(unique_games)

# creation de classe _init_ et self pour la creation des valeurs name, team, games et year

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension.name)
print(third_suspension.year)
print(third_suspension.games)

# Amelioration Classe suspension
# utilisation de la methode try pour gerer les potentielles vides
# Utilisationde classe parceque nous pouvons creer plusieurs fonctions dans une seule classe

class Suspensiontwo():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)
missing_year = Suspensiontwo(nfl_suspensions[22])
jordan = missing_year.get_year()
print (jordan)