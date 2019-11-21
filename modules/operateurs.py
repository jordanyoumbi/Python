# operateur OR and AND

a = 5
b = 10

# verifier avec boolean que a est inferieur b

result1 = (a < 5 or b> a)
print(result1)
# cela affichera True

result2 = (a < 5 and b > a)
print(result2)

# cela affichera False car ici on a la double condition qui doit etre respecter AND
