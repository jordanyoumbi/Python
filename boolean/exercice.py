int_dep_populations = [4665565556, 568856, 462358, 13855, 46655]
first_50000 = 0
first_65000 = 0
first_last = 0
nathan = int(int_dep_populations[0])
jordan = int(int_dep_populations[len(int_dep_populations) - 1])
print(nathan)

if (nathan < 500000):
   print ("le nombre est petit")
else:
   first_50000 = nathan
   print (first_50000)
#for jordan in int_dep_populations:
#    if ( 
if (nathan < 650000):
   print ("le nombre 65 est petit")
else:
   first_65000 = nathan
   print (first_65000)

if (nathan < jordan ):
   print ("le dernier numero est superieur au premier")
else:
   first_last = nathan
   print ("le premier est superieur au egal au dernier")
