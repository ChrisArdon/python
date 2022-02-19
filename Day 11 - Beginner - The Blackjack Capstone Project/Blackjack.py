import random

#Function that returns a random card from the list
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = cards[random.randint(0, 12)]
    return random_card

print(deal_card())