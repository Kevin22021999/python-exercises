print("Please enter your 3-digit pin code.")

correct_pin = "007"
count = 0
maxAttmepts = 3



while count < maxAttmepts:
    try:
        x = int(input("1."))
    except ValueError:
        print("Please enter a nummber")
    try:
        y = int(input("2."))
    except ValueError:
        print("Please enter a nummber")
    try:
        z = int(input("3."))
    except ValueError:
        print("Please enter a nummber")
    print("Please wait for confirmation...")

    entered_pin = (f"{x}{y}{z}")

    if entered_pin == correct_pin:
        print("Pin correct")
        break
    else:
        count += 1
    print("Wrong pin.\nTry again.")
if count == maxAttmepts:
    print("To many wrong attmeps. Your card has been confiscated.")