tup = (10, -3, 4, 9,12, -6, 0)



min = tup[0]
max = tup[0]
for i in tup:
    if min > i:
        min = i
    if max < i:
        max = i
print(f"Najmniejsza wartość: {min}, największa wartość: {max}")