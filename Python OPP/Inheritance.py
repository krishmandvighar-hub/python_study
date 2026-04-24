class Person:
  def __init__(self, f, l):
    self.a = f
    self.b = l

  def print(self):
    print(self.a, self.b)

#Use the Person class to create an object, and then execute the printname method:
class Student(Person):
  pass

x = Student("John", "Doe")
x.print()

#--------------------------super() function----
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)#Person.---->super().

x = Student("Mike", "Olsen")
x.printname()
#------------------------------------------------
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.brand=model
    def move(self):
        print("MOVE")

class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.brand=model
    def move(self):
        print("SAIL")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.brand=model
    def move(self):
        print("FLY")
car1=car("TESLA","MUSTARD")
boat1=boat("Great Eastern","545")
plane1=plane("INDIA","747")
##car1.move()
##boat1.move()
##plane1.move()
for x in (car1,boat1,plane1):
    x.move()













        
