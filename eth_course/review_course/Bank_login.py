print("Welcome to ABC Bank!")

username = input("Please enter your username. ")
password = input("Please enter your password. ")
pin = input("Please enter your pin. ")

correct_username = "Kevin"
correct_password = "1234"
correct_pin = "9999"

if username == correct_username and password == correct_password and correct_pin == pin:
    print(f"Welcome {correct_username}!")
else:
    print("Access denied.")