class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print("The elevator is now on floor", self.current_floor)
        return

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print("The elevator is now on floor", self.current_floor)
        return

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()
        return


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        i = 0
        while i < number_of_elevators:
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
            i = i + 1

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)
        return

    def fire_alarm(self):
        i = 0
        while i < len(self.elevators):
            elevator = self.elevators[i]
            elevator.go_to_floor(self.bottom_floor)
            i = i + 1
        return


building = Building(1, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 7)
building.run_elevator(2, 3)

building.fire_alarm()