
print('------------*Map function*------------')
def multiplyby2(nums):
    return nums * 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print('------------*multiply by 2*------------')
result = list(map(multiplyby2, numbers))

print(result)

