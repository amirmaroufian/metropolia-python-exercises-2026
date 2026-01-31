import random


points_to_generate = int(input("How many random points to generate: "))

N = 0
n = 0

if points_to_generate > 0:
    while N < points_to_generate:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y < 1:
            n += 1

        N += 1

    print(f"N: {N}, n: {n}")
    print(f"P = {4 * (n / N)}")
