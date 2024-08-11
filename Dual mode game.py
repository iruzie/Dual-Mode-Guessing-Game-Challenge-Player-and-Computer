import random

def player_guesses():
    score = 0  # Initialize the score

    while True:
        # Setting up difficulty levels
        difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
        if difficulty == "easy":
            x = 10
            guess_limit = 7
        elif difficulty == "medium":
            x = 20
            guess_limit = 5
        elif difficulty == "hard":
            x = 50
            guess_limit = 3
        else:
            print("Invalid choice, defaulting to medium.")
            x = 20
            guess_limit = 5

        random_number = random.randint(1, x)
        guess_number = None
        attempts = 0
        previous_guess = None  # Track the previous guess

        while guess_number != random_number and attempts < guess_limit:
            guess_number = int(input(f"Enter your number (between 1 and {x}): "))
            attempts += 1

            if previous_guess is not None:
                # Provide hints based on the previous guess
                if abs(guess_number - random_number) < abs(previous_guess - random_number):
                    print("Getting warmer!")
                else:
                    print("Getting colder!")

            if guess_number < random_number:
                print("Oops! Too low. Try again.")
            elif guess_number > random_number:
                print("Oops! Too high. Try again.")

            previous_guess = guess_number  # Update the previous guess

        if guess_number == random_number:
            print(f"Great job!! You guessed the secret number {random_number} right!")
            score += 1  # Increase score for a correct guess
        else:
            print(f"Sorry, you've used all {guess_limit} attempts. The secret number was {random_number}.")

        # Display score after each game
        print(f"Your current score is: {score}")

        # Play again option
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    # Display final score when the game ends
    print(f"Thank you for playing! Your final score is: {score}")

def computer_guesses():
    score = 0  # Initialize the score
    play_again = "yes"  # Start the loop

    while play_again == "yes":
        # Setting up difficulty levels
        difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
        if difficulty == "easy":
            x = 10
            guess_limit = 7
        elif difficulty == "medium":
            x = 20
            guess_limit = 5
        elif difficulty == "hard":
            x = 50
            guess_limit = 3
        else:
            print("Invalid choice, defaulting to medium.")
            x = 20
            guess_limit = 5

        low = 1
        high = x
        feedback = ''
        attempts = 0

        while feedback != 'c' and attempts < guess_limit:
            if low != high:
                guess_number = random.randint(low, high)
            else:
                guess_number = low

            attempts += 1
            print(f"Attempt {attempts}: Is it {guess_number}?")
            feedback = input(f"Is {guess_number} too high (H), too low (L), or correct (C)? ").lower()

            if feedback == 'h':
                high = guess_number - 1
            elif feedback == 'l':
                low = guess_number + 1
            elif feedback == 'c':
                print(f"Yippee! I guessed your number {guess_number} correctly!")
                score += 1
            else:
                print("Invalid input. Please enter H, L, or C.")

        if feedback != 'c':
            print(f"Sorry, I couldn't guess your number within {guess_limit} attempts.")
        
        # Display score after each game
        print(f"Your current score is: {score}")

        # Play again option
        play_again = input("Do you want to play again? (yes/no): ").lower()

    # Display final score when the game ends
    print(f"Thank you for playing! Your final score is: {score}")

def main():
    print("Welcome to the Guessing Game!")
    game_mode = input("Choose game mode: 1 for Player Guesses, 2 for Computer Guesses: ").strip()

    if game_mode == "1":
        player_guesses()
    elif game_mode == "2":
        computer_guesses()
    else:
        print("Invalid choice. Exiting the game.")

if __name__ == "__main__":
    main()
