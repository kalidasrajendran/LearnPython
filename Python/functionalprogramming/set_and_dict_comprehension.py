print('------------*set comprehension*------------')

# create a set 
my_set = set()

for char in 'hello':
    my_set.add(char)

print(my_set)


new_set = {char for char in 'hello'}
print(sorted(new_set))

new_set = {num for num in range(0,10)}
print(sorted(new_set))

new_set = {num ** 2 for num in range(0,10)}
print(sorted(new_set))

new_set = {num * 2 for num in range(0,10) if num % 2 == 0}
print(sorted(new_set))


print('------------*dict comprehension*------------')

simple_dict = {
    'a':1, 
    'b':2, 
    'c':3, 
    'd':4
    }

new_dict = {key:value ** 2 for key, value in simple_dict.items()}
print(new_dict)

new_dict = {key:value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(new_dict)

my_dict = {num:num*2 for num in [1, 2, 3]}
print(my_dict)
