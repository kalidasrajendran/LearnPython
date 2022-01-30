
my_list = []

for char in 'hello':
    my_list.append(char)


print('------------*list comprehension*------------')

new_list = [char for char in 'hello']
print(new_list)

new_list = [num for num in range(0,10)]
print(new_list)

new_list = [num ** 2 for num in range(0,10)]
print(new_list)

new_list = [num * 2 for num in range(0,10) if num % 2 == 0]
print(new_list)