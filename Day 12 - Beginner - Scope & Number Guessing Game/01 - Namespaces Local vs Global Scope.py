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