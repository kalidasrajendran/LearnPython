print('-----------*oop inheritance*-----------')

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)

x = Person("Ramya", "Jagadeesan")
x.printname()

s1 = Student('kalidas', 'Rajendran', 2013)
s1.printname()
s1.welcome()