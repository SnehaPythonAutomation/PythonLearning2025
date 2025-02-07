# Abstraction - OOPs
# It means Hiding the details and showing the what is required

# Car-> start engine -> put gear -> start driving
# but do you know how engine started ? how gear box managed?
# hide the implimentation and show only the important details

# to represent complex system by simplifying and hinding the unnecessary details

# imp-> # Abstract class cannot be initialted means you cannot create object to call because iths @abstractmethod
        # If ABC is class with incomplete 2 method, Who ever extend the class they need to complete the functions
        # In python ABC are created using ABC metaclass from the abc module



from abc import ABC, abstractmethod   # abc -module, (ABC - class , abstractmethod-function) both are them your importing


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bow Bow"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Tiger(Animal):
    def sound(self):
        return "Roar,.Roar..GRR!!"


dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())

tiger = Tiger()
print(tiger.sound())

