import random

switchOptions = {1: "Easy", 2: "Medium", 3: "Hard", 4: "Extreme", 5: "Exit"}
mode_ranges = {1: 100, 2: 1000, 3: 100000, 4: 1000000}
max_attempts = {1: 10, 2: 20, 3: 30, 4: 40}


def exit_game():
    print("Thank you for your time!!")
    return


def attempt_loop(target_val, max_attempt):
    for attempts in range(1, max_attempt + 1):
        try:
            guess = int(input("Enter your guess number: "))
        except ValueError:
            print(f"Please put a valid integer. (Range: 1 to {mode_ranges.get(3, 100000)})")
            continue

        if guess == target_val:
            # Player wins!
            print(f"You won in {attempts} attempts!")
            break

        # Determine hint direction
        hint = "Higher!" if guess < target_val else "Lower!"

        # Calculate remaining attempts for display
        remaining = max_attempt - attempts
        plural = "attempts" if remaining > 1 else "attempt"

        # Check if it was the last attempt
        if attempts == max_attempt:
            print(f"Game Over. The Target Number was {target_val}")
            break

        # Provide hint and remaining count
        print(hint)
        print(f"You have {remaining} {plural} left")

    return


def extreme_mode(target_val, max_attempt):
    print("You have 40 attempts. Guess between 1 to 1,000,000")
    print("Good luck!")
    attempt_loop(target_val, max_attempt=40)


def hard_mode(target_val, max_attempt):
    print("You have 30 attempts. Guess between 1 to 100,000")
    print("Good luck!")
    attempt_loop(target_val, max_attempt=30)


def medium_mode(target_val, max_attempt):
    print("You have 20 attempts. Guess between 1 to 1,000")
    print("Good luck!")
    attempt_loop(target_val, max_attempt)


def easy_mode(target_val, max_attempt):
    print("You have 10 attempts. Guess between 1 to 100")
    print("Good luck!")
    attempt_loop(target_val, max_attempt)


def select_difficulty(choice):
    option = choice
    mode = switchOptions.get(option, "unknown")

    # Get max attempts for this mode (default to 10 if not found)
    max_attempt = max_attempts.get(option, 10)

    # Get max range for this mode (default to 100 if not found)
    max_val = mode_ranges.get(option, 100)

    # Generate the secret number
    target_val = random.randint(1, max_val)

    if mode == "Easy":
        easy_mode(target_val, max_attempt)
    elif mode == "Medium":
        medium_mode(target_val, max_attempt)
    elif mode == "Hard":
        hard_mode(target_val, max_attempt)
    elif mode == "Extreme":
        extreme_mode(target_val, max_attempt)
    else:
        exit_game()

    return None


def main():
    print("Welcome to Guess the Number Game")
    print("--------------------------------")
    print("Please choose difficulty:")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    print("4: Extreme")
    print("5: Exit Game")

    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    select_difficulty(choice)


if __name__ == "__main__":
    main()