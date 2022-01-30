
print('------------*filter function*------------')
def only_odd(nums):
    return nums % 2 != 0

def only_even(nums):
    return nums % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print('------------*odd filter*------------')
result = list(filter(only_odd, numbers))
print(result)

print('------------*even filter*------------')
result = list(filter(only_even, numbers))
print(result)

