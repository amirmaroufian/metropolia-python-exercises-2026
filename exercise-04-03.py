number = input("Enter a number: ")

if number != "":
    largest = smallest = int(number)

    while number != "":
        num = int(number)

        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

        number = input("Enter a number: ")

    print(f"Largest: {largest}, Smallest: {smallest}")