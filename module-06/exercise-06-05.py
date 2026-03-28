def return_even_numbers(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

numbers = [1, 2, 3, 4]
print(f"Original numbers: {numbers}")
print(f"Cut-down list: {return_even_numbers(numbers)}")