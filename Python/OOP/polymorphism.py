class shape:
    def __init__(self, a, b):
        self.width = a
        self.height = b
    
    def getarea(self):
        print('area is not supported for shape')

class rectangle(shape):
    def __init__(self, a, b):
        shape.__init__(self, a, b)

    def getarea(self):
        print('area of rectangle is: ', self.width * self.height)

class triangle(shape):
    def __init__(self, a, b):
        shape.__init__(self, a, b)

    def getarea(self):
        print('area of triangle is: ', (self.width * self.height) / 2)

shape_ = shape(5, 10)    
rec = rectangle(5, 10)
tri = triangle(5, 10)

print(shape_.getarea());
print(rec.getarea());
print(tri.getarea());

shape_ = rec
print(shape_.getarea());

shape_ = tri
print(shape_.getarea());