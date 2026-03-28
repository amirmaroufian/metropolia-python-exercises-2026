numbers = []

number = input("Enter a number: ")

while number != "":
    numbers.append(int(number))
    number = input("Enter another number: ")

numbers.sort(reverse=True)

for n in numbers[:5]:
    print(n)