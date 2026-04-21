print("WELCOME TO THE BANK YOU TRUST")
x = float(input("How much CHF. do you want to withdraw? "))
print(f"You want to withdraw {x:.2f} CHF\nPlease wait...")

hundreds = x // 100
x = x % 100
fifthies = x // 50
x = x % 50
twenties = x // 20
x = x % 20
tens = x // 10
x = x % 10
print(f"100 notes: {hundreds:,.0f}\n50 notes: {fifthies:,.0f}\n20 notes: {twenties:,.0f}\n10 notes: {tens:,.0f}\nRest: {x:.2f} CHF")
if x > 0:
    print("The amount you want to withdraw cannot be dispensed. This ATM only dispenses 100, 50, 20 and 10 CHF notes.")