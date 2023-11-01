
# Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the
# main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car
# is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1",
# "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed: The
# speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is
# done using the accelerate method. Each car is made to drive for one hour. This is done with the drive method. The
# race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car
# are printed out formatted into a clear table.

import random

class Car():

    def __init__(self, rnumb, mspd):
        self.registration = rnumb
        self.maximum = mspd
        self.cspd = 0
        self.tdist = 0


    def acceleration(self, spd_acc):
        if spd_acc > 0:
            self.cspd = min(self.cspd + spd_acc, self.maximum)

        elif spd_acc < 0:
            self.cspd = max(self.cspd + spd_acc, 0)

    def drive(self, hours):
        self.tdist += hours * self.cspd

car_list = []
for i in range(1, 11):
    rnumb = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(rnumb, max_speed)
    car_list.append(car)

race = True
race_distance = 10000

hour = 1
while race:
    print(f"Hour {hour} of the race:")
    for car in car_list:
        car.acceleration(random.randint(-10, 15))
        car.drive(1)
        print(f"Car {car.registration}: Speed = {car.cspd} km/h, Traveled Distance = {car.tdist} km")

    for car in car_list:
        if car.tdist >= race_distance:
            race = False
            break

    hour += 1

print(f"{'Registration Number':<15} {'Maximum Speed (km/h)':<20} {'Final Speed (km/h)':<20} {'Traveled Distance (km)':<25}")
for car in car_list:
    print(f"{car.registration:<15}     {car.maximum:<20} {car.cspd:<20} {car.tdist:<25}")