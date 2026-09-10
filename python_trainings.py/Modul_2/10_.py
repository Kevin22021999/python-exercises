import random




correct = random.randrange(0,101,1)
attempts = 0
guess = ""

while guess != correct:
    while True:
        try:
            guess = int(input("Guess a number:"))
            break
        except ValueError:
            print("Please enter a integer")
    if guess < correct:
        print("Bigger")
    if guess > correct:
        print("Smaller")
    attempts += 1
if guess == correct:
    print(f"You guessed correctly!\nUsed attempts:{attempts}")