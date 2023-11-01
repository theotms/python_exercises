# Write a Car class that has the following properties: registration number, maximum speed, current speed and
# travelled distance. Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where
# you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties
# of the new car.

class Car():
    cspd = 0
    tdist = 0
    def __init__(self, rnumb, mspd):
        self.registration = rnumb
        self.maximum = mspd

NewCar = Car('ABC-123', 142)

print(NewCar.registration, NewCar.maximum, Car.cspd, Car.tdist)
