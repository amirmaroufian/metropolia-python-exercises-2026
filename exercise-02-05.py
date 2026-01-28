talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert everything to lots
total_lots = talents * 20 * 32 + pounds * 32 + lots

# Convert lots to grams
total_grams = total_lots * 13.3

# Convert grams to kilograms and remaining grams
total_kg = total_grams / 1000
kilograms = int(total_kg)
grams = (total_kg - kilograms) * 1000


print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")