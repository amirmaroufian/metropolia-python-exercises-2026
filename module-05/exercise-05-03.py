number = int(input("Enter a number: "))

if number < 2:
    print("It's not a prime")
else:
    prime = True

    for n in range(2, number):
        if number % n == 0:
            prime = False
            break

    if prime:
        print("It's prime")
    else:
        print("It's not prime")


