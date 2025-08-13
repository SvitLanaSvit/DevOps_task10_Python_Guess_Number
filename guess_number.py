import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    max_attempts = 5

    print("Welcome to the Guess the Number game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while number_of_attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
            number_of_attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if user_guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {number_of_attempts} attempts.")
                break
            elif user_guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if number_of_attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

guess_number()