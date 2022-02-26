
import random
print("Welcome to the Number Guessing Game!")

# Random number between 1 and 100
number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Giving the number of attempts based on the difficulty level
if difficulty == 'easy':
    attempts = 9
else:
    attempts = 4

is_finished = False

while not is_finished:
    print(f"You have {attempts + 1} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    # if the guess is equal to the number we finish the game
    if guess == number:
        print(f"You got it! The answer was {number}.")
        is_finished = True
    # If the guess is too high or too low
    elif guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")

    # Verifying the number of attempts remaining
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        is_finished = True
    else:
        print("Guess again.")

    # we reduce by 1 the number of attempts each time
    attempts -= 1
