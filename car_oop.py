class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."
    def drive_car(self):
        self.condition = "used"

# Create a class ElectricCar that inherits from Car.
class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
    # Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own drive_car() method
    # that has different functionality than the original Car class's.
    def drive_car(self):
        self.condition = "like new"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition

my_car.drive_car()
print my_car.condition


my_car = ElectricCar("molten salt", "DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition