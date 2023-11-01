# Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method
# increases the travelled distance by how much the car has travelled in constant speed in the given time. Example:
# The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases
# the travelled distance to 2090 km.

class Car():
    cspd = 0
    tdist = 0
    def __init__(self, rnumb, mspd):
        self.registration = rnumb
        self.maximum = mspd


    def acceleration(self, spd_acc):
        if spd_acc > 0:
            self.cspd = min(self.cspd + spd_acc, self.maximum)

        elif spd_acc < 0:
            self.cspd = max(self.cspd + spd_acc, 0)

    def drive(self, hours):
        self.tdist += hours * self.cspd

NewCar = Car('ABC-123', 142)

NewCar.acceleration(30)
NewCar.acceleration(70)
NewCar.acceleration(50)
NewCar.drive(2)

print(f"The registration number is: {NewCar.registration}\n"
      f"The maximum speed is: {NewCar.maximum}\n"
      f"The current speed is: {NewCar.cspd}\n"
      f"The traveled distance during was updated. Shows {NewCar.tdist}.")

print("The car brakes hard.")

NewCar.acceleration(-200)

print(f"Final speed is {NewCar.cspd}")
