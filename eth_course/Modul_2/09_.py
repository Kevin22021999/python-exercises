print("Please enter your 3-digit pin code.")
x = int(input("1. "))
y = int(input("2. "))
z = int(input("3. "))
print(f"You have entered:{x}{y}{z}")

if x == 0 and y == 0 and z == 7:
    print(f"You've entered: {x}{y}{z}")
else:
    count = 0
    if i in range(3):
        user_input = input
        print("WRONG PIN!\nTry again")
    x = int(input("1. "))
    y = int(input("2. "))
    z = int(input("3. "))