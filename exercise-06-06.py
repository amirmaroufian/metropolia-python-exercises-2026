def pizza_price_calculator(diameter, price):
    pizza_radius = diameter / 2
    pizza_area = 3.14 * (pizza_radius * pizza_radius)
    pizza_area_in_meters = pizza_area / 10000
    return price / pizza_area_in_meters

first_pizza_diameter = float(input("Enter the diameter of the first pizza: "))
first_pizza_price = float(input("Enter the price of the first pizza: "))

second_pizza_diameter = float(input("Enter the diameter of the second pizza: "))
second_pizza_price = float(input("Enter the price of the second pizza: "))


first_pizza_result = pizza_price_calculator(first_pizza_diameter, first_pizza_price)
second_pizza_result = pizza_price_calculator(second_pizza_diameter, second_pizza_price)

if first_pizza_result < second_pizza_result:
    print("First pizza's price is better")
else:
    print("Second pizza's price is better")
