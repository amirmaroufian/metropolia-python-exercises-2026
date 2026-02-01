def convert_american_gallons_to_litres(gallons):
    return gallons * 3.78541

gallons = float(input("Enter number of gallons: "))

while gallons >= 0:
    litres = convert_american_gallons_to_litres(gallons)
    print(f"{gallons} gallons equals to {litres} litres")
    gallons = float(input("Enter number of gallons: "))


