minimum_age = 18


#Reservations
reservated = "Kevin"
print("Welcome to ABC!")

name = input("Please enter your name. ")
age = int(input("Please enter your age. "))

if name == reservated:
    print(f"Welcome {name}.")
elif age >= minimum_age:
    print(f"Welcome {name}.")
else:
    print("Sory, you can not enter.")