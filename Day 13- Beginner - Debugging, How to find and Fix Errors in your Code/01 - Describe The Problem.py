############DEBUGGING#####################

# # Describe Problem
# def my_function():
#     for i in range(1, 20): #the variable i only takes values from 1 to 19. It doesn't take the 20'
#         if i == 20: #And because i never gets to 20, it doesn't print anything
#             print("You got it")
# my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"] #indexes 0 - 5
# dice_num = randint(1, 6) #here we pick a number from 1 to 6
# print(dice_imgs[dice_num]) #when we get dice_imgs[6], that element doesn't exist. Also it doesn't take dice_imgs[0]


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: # 1994 is not less than 1994
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")


# # Fix the Errors
# age = input("How old are you?") #the age here is taken as a string, not as an integer
# if age > 18:
#     print("You can drive at age {age}.") #it is not an f string


# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    # We are adding the item outside the loop. It should be inside.
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
