zander_length_cm = int(input("Enter the length of the zander in centimeters: "))

if zander_length_cm < 42:
    print("Release the fish back into the lake")
    print(f"{42 - zander_length_cm} centimeters below the size limit")
else:
    print("Great!")

