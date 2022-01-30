
print('------------*lambda function*------------')


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print('------------*multiply by 2 by lambda*------------')
result = list(map(lambda item: item * 2, numbers))
print(result)

print('------------*square by lambda*------------')
result = list(map(lambda item: item ** 2, numbers))
print(result)


print('------------*List sorting by lambda*------------')
a = [(1,2), (2,3), (3,4), (4,2), (5,-1), (6,1)]
a.sort()
print(a)

print('------------*List by second key*------------')
a.sort(key = lambda x: x[1])
print(a)