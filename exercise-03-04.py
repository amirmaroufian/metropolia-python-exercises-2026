year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("The entered year is a leap year")

else:
    print("The entered year is not a leap year")