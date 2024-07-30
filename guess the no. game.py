import random

def guess_number():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low. Try again!")
        elif guess > number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts.")
            break

guess_number()
