import random

def roll_the_dice():
    result = random.randint(1, 6)
    return result

result = 0

while result != 6:
    result = roll_the_dice()
    print(result)