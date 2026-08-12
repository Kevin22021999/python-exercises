withdraw = 0
rest = 0
max_withdraw = 1500
banknotes = 0

hundreds_frank_notes = 0
fifty_frank_notes = 0
twenty_frank_notes = 0
ten_frank_notes = 0

print("WELCOME TO THE BANK YOU TRUST")
print("*****************************")

withdraw = int(input("How much do you want to withdraw? "))

print(f"Amount entered: {withdraw} Fr.")

while withdraw > max_withdraw or withdraw <= 9:
    if withdraw <= 9:
        print("The chosen amount is too small. Please choose a biger amount.")
       
    else:
        print("The chosen amount is too big. Please choose a lower amount.")

    withdraw = int(input("How much do you want to withdraw? "))
    print(f"Amount entered: {withdraw} Fr.")




banknotes = input("Would you like to receive mixed banknotes or small banknotes? Please enter '1' for mixed and '2' small.")

while banknotes != "1" and banknotes != "2":
    print("Error! Wrong input. Please try again.")
    banknotes = input("Would you like to receive mixed banknotes or small banknotes? Please enter '1' for mixed and '2' small.")

if banknotes == "1":

    rounded = withdraw - withdraw %  10
    rest = withdraw % 10

    hundreds_frank_notes =withdraw // 100
    withdraw -= hundreds_frank_notes * 100
    fifty_frank_notes = withdraw // 50
    withdraw -= fifty_frank_notes * 50
    twenty_frank_notes = withdraw // 20
    withdraw -= twenty_frank_notes * 20
    ten_frank_notes = withdraw // 10
    withdraw -= ten_frank_notes * 10

    

elif banknotes == "2":

    rounded = withdraw - withdraw %  10
rest = withdraw % 10

fifty_frank_notes = withdraw // 50
withdraw -= fifty_frank_notes * 50
twenty_frank_notes = withdraw // 20
withdraw -= twenty_frank_notes * 20
ten_frank_notes = withdraw // 10
withdraw -= ten_frank_notes * 10


print("Loading... Please wait.")


if rest != 0:
    print(f"Your chosen amount will be rounded to {rounded}.")

print("You will receive:")
if hundreds_frank_notes > 0:
    print(f"100 franc notes: {hundreds_frank_notes}")
if fifty_frank_notes > 0:
    print(f"50 franc notes: {fifty_frank_notes}")
if twenty_frank_notes > 0:
    print(f"20 franc notes: {twenty_frank_notes}")
if ten_frank_notes > 0:
    print(f"10 franc notes: {ten_frank_notes}")

print(f"Rest: {withdraw}")

print(f"The amount of {rounded} is being dispensed.")