import random

print("Welcome to the Number Guessing Game!")

while True:
    # 1. Generate a random number
    comp_guess = random.randint(1, 100)
    count = 0
    max_attempts = 10  # Bonus: limit number of guesses

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")

    while count < max_attempts:
        user_input = input(f"\nAttempt {count + 1}: Enter your guess (or type 'exit' to quit): ")

        # 2. Allow exit anytime
        if user_input.lower() == 'exit':
            print("Goodbye! Thanks for playing.")
            exit()

        # 3. Check if input is a number
        if not user_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        user_guess = int(user_input)

        # 4. Check if number is within range
        if user_guess < 1 or user_guess > 100:
            print("Please guess a number **between 1 and 100**.")
            continue

        count += 1

        # 5. Compare user's guess with computer's number
        if user_guess == comp_guess:
            print(f"🎉 Correct!!! You guessed it in {count} attempt(s).")
            break
        elif user_guess > comp_guess:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

    else:
        print(f"\nYou've used all {max_attempts} attempts. The number was {comp_guess}.")

    # 6. Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.strip().lower() not in ['yes', 'y']:
        print("Thanks for playing!!!")
        break
