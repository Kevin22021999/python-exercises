print("Please enter your 3-digit pin code.")
x = int(input("1. "))
y = int(input("2. "))
z = int(input("3. "))

if x == 0 and y == 0 and z == 7:
    print(f"You've entered: {x}{y}{z}")
else:
    print("WRONG PIN")
