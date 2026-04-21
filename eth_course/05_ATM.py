print("WELCOME TO THE BANK YOU TRUST")
x = float(input("How much CHF. do you want to withdraw? "))
print(f"You want to withdraw {x:.2f} CHF\nPlease wait...")

if x > 1000: 
    print("The amount of cash that can be withdrawn is max. 1000 CHF at this ATM. Please try another amount.\n")
    continue
hundreds = x // 100
x = x % 100
fifthies = x // 50
x = x % 50
twenties = x // 20
x = x % 20
tens = x // 10
x = x % 10
if x > 0: print(f"The rest value of {x:.2f} can not be given. 10 notes are the lowest possible amount that can given")
print(f"100 notes: {hundreds:,.0f}\n50 notes: {fifthies:,.0f}\n20 notes: {twenties:,.0f}\n10 notes: {tens:,.0f}\nRest: {x:.2f} CHF")