print("Welcome to ABC Bank!")

username = input("Please enter your username. ")
password = input("Please enter your password. ")

correct_username = "Kevin"
correct_password = "1234"

if username == correct_username and password == correct_password:
    print(f"Welcome {correct_username}!")
else:
    print("Wrong username or password. Please try again.")