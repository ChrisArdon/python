############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo

#Function that returns a random card from the list
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

#function called calculate_score() that takes a List of cards as input and returns the score. 
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    #Checking for a Blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare (u_score, c_score):
    #If the computer and user both have the same score, then it's a draw.
    if u_score == c_score:
        return "Draw"
    #If the computer has a blackjack (0), then the user loses.
    elif c_score == 0:
        return "Lose, opponent has a Blackjack"
    #If the user has a blackjack (0), then the user wins.
    elif u_score == 0:
        return "Win with a Blackjack"
    #If the user_score is over 21, then the user loses.
    elif u_score > 21:
        return "You went over. You lose."
    #If the computer_score is over 21, then the computer loses.
    elif c_score > 21:
        return "Opponent went over. You win."
    #If none of the above, then the player with the highest score wins.
    else:
        if u_score > c_score:
            print("You win.")
        else:
            print("You lose.")

def play_game():
    print(logo)
    #Lists that will hold the random cards
    user_cards = []
    computer_cards = []
    test_cards = [10,11,10,10]
    
    is_game_over = False
    
    #Deal the user and computer 2 cards each using deal_card() and append().
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    #The score will need to be rechecked with every new card drawn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
            
        #If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            #If the game has not ended, ask the user if they want to draw another card.
            user_should_continue = input("Want another card?: y/n ")
            #If yes, then use the deal_card() function to add another card to the user_cards List.
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    #The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Ask the user if they want to restart the game.
while input("Do you want to play a game of Blackjack? y/n: ") == "y":
    clear()
    play_game()
