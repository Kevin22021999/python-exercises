correct_pin = "1234"
balance = 2500
max_withdraw = 1000
pin = "0000"
withdraw = 0

print("Welcome to ABC ATM. Please insert your card.")


while pin != correct_pin:
    pin = input("Enter your PIN.")
    if pin != correct_pin:
        print("Wrong PIN. Try again.")

print("Pin correct!")
print("************")
print("1. Check balance. \n2. Withdraw money. \n3.Exit")

options = input("Please choose one option. ")

while options == "1":
        print(f"Your current balance is {balance} CHF.")
        options = input("Please choose one option. ")


if options == "2":
    withdraw = int(input("How much money would you like to withdraw? "))  

    while withdraw > 0 and withdraw > max_withdraw:
        print("Chosen amount is too big. Please choose a smaller amount. ")
        withdraw = int(input("How much money would you like to withdraw? "))   

    balance -=  withdraw
    print(f"{withdraw} CHF.\nPlease take your money.\nYour current balance is {balance} CHF.") 


elif options == "3":
    print("Goodbye !")

else:
    print("Invalid option.")