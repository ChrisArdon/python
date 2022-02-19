import random

#Function that returns a random card from the list
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = cards[random.randint(0, 12)]
    return random_card

#Lists that will hold the random cards
user_cards = []
computer_cards = []

#Deal the user and computer 2 cards each using deal_card() and append().
user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(f"User: {user_cards}")
print(f"Computer: {computer_cards}")