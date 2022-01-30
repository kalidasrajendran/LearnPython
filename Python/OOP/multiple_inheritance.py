
class rectangle():
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def get_rectanglearea(self):
        print('area of rectangle is: ', self.width * self.height)

class triangle():
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def get_trianglearea(self):
        print('area of triangle is: ', (self.width * self.height) / 2)

class circle():
    def __init__(self, a):
        self.radius = a

    def get_circlearea(self):
        print('area of circle is: ', (self.radius ** 2) * 3.14)

class shape(rectangle, triangle, circle):
    def __init__(self, width, height, radius):
        rectangle.__init__(self, width, height)
        triangle.__init__(self, width, height)
        circle.__init__(self, radius)

obj = shape(5, 10, 2)

print(obj.get_rectanglearea())
print(obj.get_trianglearea())
print(obj.get_circlearea())

print(help(obj))