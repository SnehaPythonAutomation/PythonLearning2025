#Polymorphism -> Defination-> Polymorphism allows objects of different classes to be trated as objects of a common superclass
# polymorphism simply means that if you have 3 obejcts and you call the are function it will call that respected
# who ever object is created will call that area function only




class Shape:
    def area(self):
        print("Area of shape")


class Rechtangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width


    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1=Rechtangle(37,40)
print(shape1.area())

shape2=Circle(10)
print(shape2.area())

shape3=Shape()
shape3.area()