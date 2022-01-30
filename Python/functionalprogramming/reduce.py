from functools import reduce

print('------------*reduce function*------------')


numbers = [1, 2, 3]

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, numbers, 0))
print(reduce(accumulator, numbers, 10))

print(numbers)

