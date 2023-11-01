# Extend the program by adding an accelerate method into the new class. The method should receive the change of speed
# (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the
# speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50
# km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change
# on the speed and then print out the final speed. The travelled distance does not have to be updated yet.

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


NewCar = Car('ABC-123', 142)

NewCar.acceleration(30)
NewCar.acceleration(70)
NewCar.acceleration(50)

print(f"The registration number is: {NewCar.registration}\n"
      f"The maximum speed is: {NewCar.maximum}\n"
      f"The current speed is: {NewCar.cspd}\n"
      f"The traveled distance wasn't updated. Shows {NewCar.tdist}.")

print("The car brakes hard.")

NewCar.acceleration(-200)

print(f"Final speed is {NewCar.cspd}")