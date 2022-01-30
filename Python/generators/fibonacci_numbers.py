def fib(number):
    a = 0
    b = 1

    for i in range(number):
        yield a
        temp = a
        a = b
        b = a + temp


for x in fib(500):
    print(x)