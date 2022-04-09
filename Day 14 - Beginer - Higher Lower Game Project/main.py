import art
from game_data import data
import random
import os

# Function to clear the screen
def cls():
    """Function to clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# function to retrieve data given the parameter and a random index
def retrieve_data(arg, rn):
    return data[rn][arg]

# function that returns who has more followers
def who_has_more_follows(option1, option2):
    if option1 > option2:
        return "a"
    else:
        return "b"


def game():
    cls()
    # Displaying art
    print(art.logo)
    game_over = False  # Check if the game is over through the while loop
    score = 0  # Keep the score
    while not game_over:
        # Random number based on the length of the game_data
        random_number1 = random.randint(0, len(data) - 1)
        random_number2 = random.randint(0, len(data) - 1)
        # Getting data for option A
        # If the score is 0 (means if the game is starting...) We retrieve a random account
        if score == 0:
            nameA = retrieve_data("name", random_number1)
            followsA = retrieve_data("follower_count", random_number1)
            descriptionA = retrieve_data("description", random_number1)
            countryA = retrieve_data("country", random_number1)
        else:  # if we have score > 0 means we won the round. So the B pass to A
            nameA = nameB
            followsA = followsB
            descriptionA = descriptionB
            countryA = countryB

        # Formating the account data into printable format.
        print(f"Compare A: {nameA}, {descriptionA}, from {countryA}")

        print(art.vs)

        # Getting data for option B
        nameB = retrieve_data("name", random_number2)
        followsB = retrieve_data("follower_count", random_number2)
        descriptionB = retrieve_data("description", random_number2)
        countryB = retrieve_data("country", random_number2)

        print(f"Against B: {nameB}, {descriptionB}, from {countryB}")

        # We get the correct answer with the help of our function and we have the answer ready for comparison
        correct_answer = who_has_more_follows(followsA, followsB)
        #print(f"The correct answer: {correct_answer}")
        guess = input("Who has mor followers? Type 'A' or 'B': ")

        # Checking if the user guess is correct
        if(guess.lower() == correct_answer):
            score += 1
            print(art.logo)
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\n")
            game_over = True


game()
