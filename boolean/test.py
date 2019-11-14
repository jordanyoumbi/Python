# print(8 > 9 ) #ressortira la valeur "false" car 8 n' est superieur 9

f = open("test.txt", "r")
data = f.read()
rows = data.split("\n")

departement = []
int_des_populations = []

for row in rows:
    jordan = row.split(',')
#    departement.append(int(jordan[1]))
    int_des_populations.append(jordan)
print (int_des_populations)
