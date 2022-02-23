################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#### Local Scope ####
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) #We can't use inside variables outside a function

#### Global Scope ####
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)
drink_potion()
print(player_health)

##################
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

#### Example ####
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy) #The local variables only can be used inside the function

######### Modifying Global Scope #########
enemies = "Skeleton"
def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}") #Prints "Zombie"

increase_enemies()
print(f"enemies outside function: {enemies}") #Prints "Skeleton"


######### Modifying Global Scope #########
enemies = 1
def increase_enemies():
    global enemies  #If we want to modify de goblal variable in a local enviroment
    enemies += 1
    print(f"enemies inside function: {enemies}")
    
    
######### Using the Global variable without modifying it localy #########
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1 #We use a return to modify the variable localy and if we want to keep the goblal value

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")



############### Global Constants ###############
#We can use global variables as a constants
#They can be written in Uppercase to differenciate them from normal variables.
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@ChrizHellscream"