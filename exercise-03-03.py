# gender = input("Please enter your gender: ")
#
# hemoglobin = int(input("Please enter your hemoglobin: "))
#
# if gender == "male" and 134 <= hemoglobin <= 167:
#     print("Your hemoglobin value is normal")
# elif gender == "male" and hemoglobin < 134:
#     print("Your hemoglobin value is low")
# elif gender == "male" and hemoglobin > 167:
#     print("Your hemoglobin value is high")
#
# elif gender == "female" and 117 <= hemoglobin <= 155:
#     print("Your hemoglobin value is normal")
# elif gender == "female" and hemoglobin < 117:
#     print("Your hemoglobin value is low")
# elif gender == "female" and hemoglobin > 155:
#     print("Your hemoglobin value is high")

gender = input("Please enter your gender: ").lower()
hemoglobin = int(input("Please enter your hemoglobin: "))

if gender == "female":
    if 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal")
    elif hemoglobin < 117:
        print("Your hemoglobin value is low")
    elif hemoglobin > 155:
        print("Your hemoglobin value is high")

elif gender == "male":
    if 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal")
    elif hemoglobin < 134:
        print("Your hemoglobin value is low")
    elif hemoglobin > 167:
        print("Your hemoglobin value is high")

else:
    print("Gender is invalid")