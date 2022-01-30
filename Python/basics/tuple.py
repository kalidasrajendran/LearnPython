my_tuple = (1, 2, 3, 4, 5) # non mutable similar to lists except non mutability

for a in my_tuple:
    print(a)

print(5 in my_tuple)

print('-------*length*-------')
print(len(my_tuple))


print('-------*access values*-------')
x, y, *other = (1, 2, 3, 4, 5, 5)
print(x)
print(y)

print('-------*loop other*-------')
for i in other:
    print(i)

print('-------*count*-------')
print(other.count(5))


