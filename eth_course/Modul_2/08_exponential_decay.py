dose = 5.0
degaration_rate = 0.1

print("t | concentration in blood")
print("**************************")

for i in range(0, 5):
    dose = dose * (1-degaration_rate)
    print(i, " ",dose)