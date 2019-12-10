# tout d' abord il faut recuperer le mudule time
# l' exemple ci-dessous affiche le nombre de seconde depuis 1970. date à le quelle les comptes ont commencé
import time
current_time = time.time()
print(current_time)
# utilisation de function gmtime() pour connaitre l' heure GMT
current_struct_time = time.gmtime(current_time)
print(current_struct_time)
current_hour = current_struct_time.tm_hour
print(current_hour)
current_year = current_struct_time.tm_year
print(current_year)

# un autre module sur le temps: datetime. ce module est plus efficazce que le module time
import datetime
current_datetime = datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month
print(current_datetime, current_year, current_month)

# Utilisation d' un nouveau module qui est une function qui favorise aussi les calculs: timedelta

# Comment formater les dates. ici on bveux donner un format au dates: stfrtime

today = datetime.datetime(2017, 6, 16, 10, 14, 23)
print(today)
#stfrtime()
string_today = today.strftime("%b %d %Y")
print(string_today)
#pour faire le chemin inverse c' est à dire remettre le temps sous long format ont utilise: strptime
today_2 = time.strptime(string_today, "%b %d %Y")
print(today_2)

# Utiliser la focntion fromtimestamp() pour convertir un chiffre en temps lisible. c' est une fonction du module datetime
datetime_object = datetime.datetime.fromtimestamp(1440082910.0)
print(datetime_object)