# with user input

class Car():
    color = None  # attribute
    model = None
    name = None

    def car_details(self, name):  # method  # can add parametrs multiple args as well
        print("Your car details is -" + name, self.model, self.color)


car_color = input("Enter your car color")
car_model = input("Enter your car model")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model
car_obj_ref.car_details("sneha")
