# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators
# to the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is on floor {self.current_floor}")

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is on floor {self.current_floor}")

    def fire_alarm(self):
        self.current_floor = self.bottom_floor
        print(f"Fire alarm activated, elevators going to the bottom floor!")


class Building:
    def __init__(self, bottom_floor, top_floor, n_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(n_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_number} does not exist in this building.")

building = Building(1, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 1)

for elevator in building.elevators:
    elevator.fire_alarm()
