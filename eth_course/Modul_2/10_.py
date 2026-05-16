correct = 26
attemtps = 0
guess = ""

while guess != correct:
    while True:
        try:
            guess = int(input("Guess a number:"))
            number = int(guess)
            break
        except ValueError:
            print("Please enter a integer")
    if guess < correct:
        print("Bigger")
    if guess > correct:
        print("Smaller")
    attemtps += 1
if guess == correct:
    print(f"You guessed correctly!\nUsed attamps:{attemtps}.")