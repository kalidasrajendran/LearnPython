print('-----------*oop basics*-----------')

class person:
    # class object attributes
    count = 0 # more like a static variable

    @classmethod
    def add_person(cls, name, age):
        return cls('Kalidas', 30)

    @staticmethod
    def get_count():
        return person.count

    def __init__(self, name, age): # constructor
        self.name = name  # attribute
        self.age = age
        person.count = person.count + 1
        print(f'object created for person {self.name} with age {self.age}')

    def __del__(self): # destructor
        person.count = person.count - 1
        print(f'object deleted for person {self.name} with age {self.age}')

    def getname(self): # methods
        return self.name

    def getage(self):
        return self.age

print('total active persons: ', person.get_count())

p1 = person.add_person('Kalidas', 30)
p2 = person('Ramya', 26)

print('name: ', p1.getname())
print('age: ', p1.getage())

print('name: ', p2.name)
print('age: ', p2.age)

print('total active persons: ', person.get_count())


# delete p1
del p1

print('total active persons: ', person.get_count())




