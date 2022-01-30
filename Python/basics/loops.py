print('-------*If loop*-------')
# if loops

a = 10
b = 20

if a > 10:
    print('a greater than 10')
elif a < 10:
    print('a less than 10')
else:
    print('a is 10')

print('-------*true and false*-------')
# true and false
print(bool(''))
print(bool('Hallo'))

print(bool(10))
print(bool(0))


print('-------*logical operators*-------')
# logical operators
#  ==                   # equal values
#  !=                   # not equal
#  >                    # left operand is greater than right operand
#  <                    # left operand is less than right operand
#  >=                   # left operand is greater than or equal to right operand
#  <=                   # left operand is less than or equal to right operand
#  <element> is <element> # check if two operands refer to same object in memory

print(1 < 2 and 4 > 1)  # True
print(1 > 3 or 4 > 1)  # True
print(1 is not 4)  # True
print(not True)  # False
print(1 not in [2, 3, 4])  # True

print('-------*For loop*-------')
# for loops
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list2 = [(1, 2), (3, 4), (5, 6)]
my_dict = {'a': 1, 'b': 2, 'c': 3}

for num in my_list:
    print(num)  # 1, 2, 3

for num in my_tuple:
    print(num)  # 1, 2, 3

for num in my_list2:
    print(num)  # (1,2), (3,4), (5,6)

for num in '123':
    print(num)  # 1, 2, 3

for k, v in my_dict.items():  # Dictionary Unpacking
    print(k)  # 'a', 'b', 'c'
    print(v)  # 1, 2, 3


print('-------*While loop*-------')
i = 1
while i <= 50:
    print(i)
    i += 1
else:
    print('finished with while loop')





