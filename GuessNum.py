import random

switchOptions = {   1: "Easy",  2: "Medium",    3: "Hard",      4: "Extreme", 5: "Exit"}
mode_ranges = {     1: 100,     2: 1000,        3: 100000,      4: 1000000 }
max_attempts = {    1: 10,      2: 20,          3: 30,          4: 40 }


def exit_game():
    print("Thank you for your time!!")
    return


def attempt_loop(target_val, max_attempt):
    for attempts in range(1, max_attempt + 1):
        try:
            guess = int( input("Enter your guess number: "))
        except ValueError:
            print("Please put valid input (1 to 100).")
            continue

        if guess == target_val:
            print(f"You won in {attempts} attempts")
            break

        print(target_val)

        hint = "Higher!" if guess < target_val else "Lower!"

        remaining = max_attempt - attempts
        plural = "attempts" if remaining > 1 else "attempt"

        if attempts == max_attempt:
            print(f"Game Over. The Target Number is {target_val}")
            break

        if guess < target_val:
            print(hint)
            print(f"You have {max_attempt - attempts} {plural} left")
        elif guess > target_val:
            print(hint)
            print(f"You have {max_attempt - attempts} {plural} left")


    return


def extreme_mode(target_val, max_attempt):
    print("You have 10 attempts. Guess between 1 to 1000000")
    print("Good luck")

    attempt_loop(target_val, max_attempt=40)

    pass


def hard_mode(target_val, max_attempt):
    print("You have 10 attempts. Guess between 1 to 100000")
    print("Good luck")

    attempt_loop(target_val, max_attempt=30)

    pass


def medium_mode(target_val, max_attempt):
    print("You have 10 attempts. Guess between 1 to 1000")
    print("Good luck")

    attempt_loop(target_val, max_attempt)

    return


def easy_mode(target_val, max_attempt):
    print("You have 10 attempts. Guess between 1 to 100")
    print("Good luck")

    attempt_loop(target_val, max_attempt)

    return


def select_difficulty(choice):
    option = choice
    mode = switchOptions.get(option, "unknown")

    max_attempt = max_attempts.get(option, 10)

    max_val = mode_ranges.get(option, 10)
    target_val = random.randint(1, max_val)

    if   mode == "Easy":        easy_mode(target_val, max_attempt)
    elif mode == "Medium":      medium_mode(target_val, max_attempt)
    elif mode == "Hard":        hard_mode(target_val, max_attempt)
    elif mode == "Extreme":     extreme_mode(target_val, max_attempt)
    else :                      exit_game()

    return None


def main():
    print("Welcome to Guess the Number Game")
    print("--------------------------------")
    print("Please choose difficulty")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    print("4: Extreme")
    print("5: Exit Game")

    choice = int ( input("Choice: ") )
    select_difficulty(choice)


if __name__ == "__main__":
    main()


