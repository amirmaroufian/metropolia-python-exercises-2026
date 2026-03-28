real_username = "python"
real_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == real_username and password == real_password:
        print("Welcome")
        break

    attempts += 1
else:
    print("Access denied")