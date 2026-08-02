

minimum_age = 18


#Reservations
reservated = "Kevin"
print("Welcome to ABC!")

booking = input("Please enter your name. ")
age = int(input("Please enter your age. "))

if booking == reservated:
    print(f"Welcome {booking}.")
elif age >= minimum_age:
    print(f"Welcome {booking}.")
else:
    print("Sory, you can not enter.")