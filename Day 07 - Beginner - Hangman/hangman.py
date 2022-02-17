import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
display = []

#For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(word_length):
    display += "_"


end_of_game = False

#Check guessed letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
        
    for position in range(word_length):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter
            
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1    
    
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives <= 0:
        end_of_game = True
        print("You Lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    #Import the stages from hangman_art.py
    print(hangman_art.stages[lives])