import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.car_list:
            print(f"Car {car.registration_number} - Current speed: {car.current_speed} km/h - Maximum speed: {car.maximum_speed} km/h - Travelled distance: {car.travelled_distance} km")
        print()

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.kilometers:
                return True
        return False

cars = []
for i in range(10):
    car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        race.print_status()

race.print_status()