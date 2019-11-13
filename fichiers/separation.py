# transformer des chaines de caracteres en liste
# split()
names="Tom,seb,bob"
split_list = names.split(",") # la fonction separera les caracteres àhaque fois qu' ele rencontrera une virgule
print(split_list)

data = open("data", "r") 
jordan = data.read()
split_jordan = jordan.split("\n")
print(split_jordan)
print(split_jordan[0:5])
