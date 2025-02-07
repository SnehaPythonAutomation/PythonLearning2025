# Constructor->Way to initialize objects attributes
# create constructer with __init__() method

#if you want to set initial value then use constructor ..when you call object car() then this funtion __init__ auto call
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("I will be called first")

    def start_engine(self):
        print("Starting..", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine()
car2.start_engine()

# Object is created a special function is called automatically __init__()
# All the attribute object you can initialize- add some initial value to them

#Car has Class which has two attributres to initialize you can create constructor ..constructor is called whenever
# object(Car("Toyota", "Camry")) is created