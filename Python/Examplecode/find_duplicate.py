list_value = ['a', 'a', 'b', 'c', 'd', 'e', 'd']

# only duplicate
duplicated = []

for value in list_value:
    if list_value.count(value) > 1:
        if value not in duplicated:
            duplicated.append(value)

dup = list(set([x for x in list_value if list_value.count(x) > 1]))

print('duplicate values: ', sorted(dup))
print('duplicate values: ', duplicated)

# unique values
unique = []

for value in list_value:
    if value not in unique:
        unique.append(value)

print('unique values: ', unique)

unique = []
