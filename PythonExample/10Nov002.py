# Overriding -> overriding means same name in the parent and child(Same function with the same name)
# Super() means call my parent fun to

class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()  # we are calling here both paraent and child functions using super(). function if we use only dog=Dog() object

    print("Dog sound")


#  pass

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()
