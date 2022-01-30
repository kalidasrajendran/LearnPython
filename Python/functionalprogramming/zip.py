
print('------------*zip function*------------')


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers3 = ['a', 'b', 'c', 'd', 'h', 's', 't', 'a']

print('------------*zips item together*------------')
result = list(zip(numbers1, numbers2, numbers3))
# creates a lists with tuples
print(result) # [(1, 1, 'a'), (2, 2, 'b'), (3, 3, 'c'), (4, 4, 'd'), (5, 5, 'h'), (6, 6, 's'), (7, 7, 't'), (8, 8, 'a')]

