airport_data = {}

while True:
    action = int(input("Choose the action by entering a number:\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\n: "))

    if action == 1:
        airport_name = input("Enter the airport name: ")
        airport_ICAO = input("Enter the airport ICAO: ")

        airport_data[airport_ICAO] = airport_name

        print("Airport added successfully")
    elif action == 2:
        airport_ICAO = input("Enter the airport ICAO: ")

        if airport_ICAO in airport_data:
            print(f"{airport_ICAO}: {airport_data[airport_ICAO]}")
        else:
            print("Airport not found")
    elif action == 3:
        break