def sum_of_list_numbers(numbers_list):
    total = 0
    for n in numbers_list:
        total += n
    return total

numbers = []

number = (input("Enter a number: "))

while number != "":
    numbers.append(int(number))
    number = (input("Enter a number: "))

print(f"Sum of numbers: {sum_of_list_numbers(numbers)}")
