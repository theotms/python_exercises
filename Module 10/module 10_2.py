
# Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers
# of the bottom and top floors and the number of elevators in the building. When a building is created, the building
# creates the required number of elevators. The list of elevators is stored as a property of the building. Write a
# method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In
# the main program, write the statements for creating a new building and running the elevators of the building.

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
