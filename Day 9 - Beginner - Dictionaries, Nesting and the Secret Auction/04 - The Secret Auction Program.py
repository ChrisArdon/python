from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art 

#We print the logo from the art file
print(art.logo)

#Variable to control if there are more players
bidding_finished = False

#Creating the empty dictionary  that will hold the players
players = {
    #Name : Bid
}

while not bidding_finished:
    #Inputs
    name = input("What is your name? ")
    bid = input("What is your bid? $")   

    #Insert the player into the dictionary
    players[name] = bid

    #Asking if there are other players
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if (should_continue == "Yes") or (should_continue == "yes"):
        #if we have more players we clear the screen
        clear()
    else:
        #if not we end the while loop
        bidding_finished = True

#Temporal variable to sort the highest BID
maximum = 0
#Variable that will hold the winner based on the key
winner = ""

for key in players:
    #We convert the BID to int
    bid_int = int(players[key])
    if(bid_int > maximum):
        maximum = bid_int
        winner = key

#Printing the output
print(f"The winner is {winner} with a BID of ${maximum}")