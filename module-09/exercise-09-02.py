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


car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed after acceleration: {car.current_speed} km/h")

car.accelerate(-200)

print(f"Final speed after braking: {car.current_speed} km/h")