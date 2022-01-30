
print('----*generator example*----')
def generator_functions(num):
    for i in range(num):
        yield i


for item in generator_functions(10):
    print(item)

print('----*next example*----')
g = generator_functions(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print('----*under the hood of the generators*----')

def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      next(iterator)
    except StopIteration:
      break


special_for([1, 2, 3, 4, 5])




