import random

dices_to_roll = int(input("How many dices to roll: "))

dices = []
rolls = 0

while rolls < dices_to_roll:
    dices.append(random.randint(1, 6))
    rolls += 1

# print(dices)
sum_of_dices = 0

for n in dices:
    sum_of_dices += n

print(f"Sum: {sum_of_dices}")

# import random
#
# dices_to_roll = int(input("How many dices to roll: "))
#
# sum_of_rolls = 0
#
# for n in range(dices_to_roll):
#     roll = random.randint(1, 6)
#     sum_of_rolls += roll
#     print(roll)
#
# print(f"Sum is: {sum_of_rolls}")