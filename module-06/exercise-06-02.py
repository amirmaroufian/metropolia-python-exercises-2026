import random

def roll_the_dice(dice_sides):
    result = random.randint(1, dice_sides)
    return result

result = 0

dice_sides = int(input("Enter the number of sides: "))

while result != dice_sides:
    result = roll_the_dice(dice_sides)
    print(result)