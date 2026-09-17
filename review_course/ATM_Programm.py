correct_pin = "1234"
withdrawlimit = 1500

print("Welcome to ABC Bank.")
pin = input("Please enter your PIN. ")

if pin == correct_pin:
    print("Login successful!")
    money = int(input("How much money would you like to withdraw? "))

    if money <= withdrawlimit:
        print("Please take your cash.")
    else:
        print("Insufficient witdrawal limit.")

else:
    print("Access denied.")