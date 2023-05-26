import random

def guess_the_number():
    print("Welcome to Guess the Number game!")
    min_range = 1
    max_range = 100
    number = random.randint(min_range, max_range)
    attempts = 0

    while True:
        guess = int(input(f"Guess a number between {min_range} and {max_range}: "))
        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thank you for playing. Goodbye!")

guess_the_number()
