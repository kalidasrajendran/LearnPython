def printfunction(data):
    print(data)


printfunction('test')


def twoparam(data1, data2=10):
    print(data1, data2)


twoparam(1, 2)
twoparam(1)


def manyparam(*args):
    for item in args:
        print(item, end=' ')
    print()

manyparam('1', '2', '3', '4')

def by_name(data1, data2, data3):
    print(data1, data2, data3)


by_name(data3=3, data1=1, data2=2)


def keywordargu(**kwargs):
    print("His last name is " + kwargs["lname"])


keywordargu(fname="kalidas", lname="Rajendran")




