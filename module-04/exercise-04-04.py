import random

actual_number = random.randint(1, 10)

user_number = int(input("Enter a number: "))

while user_number != actual_number:
    if user_number > actual_number:
        print("Too high")
    elif user_number < actual_number:
        print("Too low")

    user_number = int(input("Enter a number: "))

print("Correct")