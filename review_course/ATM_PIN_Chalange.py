correct_pin = "1234"
pin = "0000"

while pin != correct_pin:
    pin = input("Enter your PIN. ")
    if pin != correct_pin:
        print("Wrong PIN. Try again. ")
print("Welcome!")
 