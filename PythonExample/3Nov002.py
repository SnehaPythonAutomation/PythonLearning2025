#Car-
#Objects- Tesla, Lambo

class Car:
    name=None
    color=None
    model=None
    speed=None
    engine=None

    def start_engine(self):         # self is special veriable that is used within the context of Object-Oriented Programming
        print("starting engine")    # It is a reference to instance of a class
                                    # It helps to access and manipulate the attributes and methods of the intance
    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving->" +self.name)  # you can access manipulate using self.

tesla_obj=Car()   # tHis is instance of a class - object
lambo_obj=Car()   # tHis is instance of a class - object

tesla_obj.name = "Tesla"
lambo_obj.name= "lambo"

tesla_obj.who_is_driving()  # now you can differenctiate by adding +self.name in method like who is driving by name
lambo_obj.who_is_driving()
