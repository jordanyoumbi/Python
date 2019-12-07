values = [None, 1, 45, None, 75]
check = [x is not None and x > 30 for x in values]
print(check)