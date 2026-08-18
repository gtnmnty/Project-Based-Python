import random

target = random.randint(1, 100)
maxAttempt = 10

print("Welcome to Guess the Number Game")
print(f"Guess between 1 and 100. You have {maxAttempt} attempts.")

for remaining in range(maxAttempt, 0, -1):
    try:
        guess = int( input("Enter the number: ") )
    except ValueError:
        print("Please put valid input (1 to 100).")
        continue

    if guess == target:
        attempts = (maxAttempt - remaining) + 1
        print(f"You won in {attempts}!")
        break

    attempt_left = remaining - 1

    hint = "Higher!" if guess < target else "Lower!"

    if attempt_left == 0:
        print("Game Over")

    if guess < target:
        print(hint)
        print(f"You have {attempt_left} attempts left")

    elif guess > target:
        print(hint)
        print(f"You have {attempt_left} attempts left")

