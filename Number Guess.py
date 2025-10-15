# guess.py

import random

print("Number Guessing Game")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or 'q' to quit): ")

    if guess.lower() == 'q':
        print(f"The number was {number}. Exiting game.")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Enter a valid number.")
        continue

    attempts += 1

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
