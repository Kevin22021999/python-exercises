withdraw = 0
rest = 0

print("WELCOME TO THE BANK YOU TRUST")
print("*****************************")

withdraw = int(input("How much do you want to withdraw? "))

print(f"Amount entered: {withdraw} Fr.")


rounded = withdraw - withdraw %  10
rest = withdraw % 10

hundreds_frank_notes =withdraw // 100
withdraw -= hundreds_frank_notes * 100
fifty_frank_notes = withdraw // 50
withdraw -= fifty_frank_notes * 50
twenty_frank_notes = withdraw // 20
withdraw -= twenty_frank_notes * 20
ten_frank_notes = withdraw // 10
withdraw %= ten_frank_notes * 10



print("Loading... Please wait.")

if rest != 0:
    print(f"Your chosen amount will be rounded to {rounded}.")

print("You will receive:")
print(f"100 franc notes: {hundreds_frank_notes}")
print(f"50 franc notes: {fifty_frank_notes}")
print(f"20 franc notes: {twenty_frank_notes}")
print(f"10 franc notes: {ten_frank_notes}")
print(f"Rest: {withdraw}")

print(rounded)