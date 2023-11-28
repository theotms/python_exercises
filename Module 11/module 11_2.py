# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have
# the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in
# liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars
# receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of
# the base class to set the first two properties and then sets its capacity. Write a main program where you create
# one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for
# both cars, make them drive for three hours and print out the values of their kilometer counters.]

class Car():

    def __init__(self, rnumb, mspd):
        self.registration = rnumb
        self.maximum = mspd
        self.cspd = 30
        self.tdist = 0

    def acceleration(self, spd_acc):
        if spd_acc > 0:
            self.cspd = min(self.cspd + spd_acc, self.maximum)

        elif spd_acc < 0:
            self.cspd = max(self.cspd + spd_acc, 0)

    def drive(self, hours):
        if self.cspd > 0:
            self.tdist += hours * self.cspd

class ElectricCar(Car):
    def __init__(self, rnumb, mspd, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(rnumb, mspd)


class GasolineCar(Car):
    def __init__(self, rnumb, mspd, tank):
        self.tank = tank
        super().__init__(rnumb, mspd)

car = []
car.append(ElectricCar("ABC-15", 180, 52.5))
car.append(GasolineCar("ACD-123", 165, 32.3))

for e in car:
    e.drive(2)
    print(e.tdist)

"""
ecar = ElectricCar("ABC-15", 180, 52.5)
gcar = GasolineCar("ACD-123", 165, 32.3)
ecar.drive(2)
gcar.drive(2)

print("Electric Car Total Distance:", ecar.tdist)
print("Gasoline Car Total Distance:", gcar.tdist)
"""